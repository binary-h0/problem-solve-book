from 백준 import Connector
import os
import shutil
import json

class Analyzer:
    def __init__(self):
        self.connector = Connector.Connector()
        self.path = self.connector.getPath()
        self.problemListPath = "../problem_list/"
        self.problemList = []
        self.updateProblemList = []
        self.deleteProblemList = []
        self.issueFileList = []
        self.issueTypes = ['Not Update Memory', 'File Changed', 'File Deleted']
        self.fileTypes = {'py':0, 'cpp':1, 'c':2, 'go':3, 'txt':4, 'pyc':5}
        self.fileLists = [[] for _ in range(len(self.fileTypes))]
        self.setAllFileList()
        self.setProblemList()
    def setAllFileList(self):
        for root, directories, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                file_path = file_path.split('.')
                type = file_path[-1]
                path = '.'.join(file_path)
                self.fileLists[self.fileTypes[type]].append([path, 0])
    def getFileList(self):
        return self.fileLists
    def setProblemList(self):
        for files in self.fileLists:
            for file in files:
                token = file[0].split('/')
                token1 = token[-1].split('.')
                if token1[0].isdigit():
                    self.problemList.append(int(token1[0]))
                    file[1] = int(token1[0])
            files.sort(key=lambda x:x[1])
        self.problemList.sort()
    def printPath(self):
        print(self.path)
    def printAllFilePath(self):
        for root, directories, files in os.walk(self.path):
            for file in files:
                file_path = os.path.join(root, file)
                print(file_path)
    def copyAllFileToMemory(self, copyPathLists):
        paste_folder_path = self.problemListPath
        for copyPath in copyPathLists:
            token = copyPath.split('/')
            shutil.copyfile(copyPath, paste_folder_path + token[-1])
    def createJson(self):
        object = {
                  "baekjoon" : {
                    "total" : 0,
                    "problems" : [

                    ],
                    "issue": {
                      "white_problem": [

                      ],
                      "black_problem": [

                      ]
                    }
                  }
                }
        with open("problem_analyzer/problem_list.json", 'w') as memory:
            json.dump(object, memory, indent=2)
    def updateJson(self, object):
        with open("problem_list.json", 'w') as db:
            json.dump(object, db, indent=2)
    def setUpdateFileList(self, j_lis, m_lis):
        idx_j, idx_m = 0, 0
        if len(j_lis) == 0:
            print("INIT")
            return m_lis
        if len(j_lis) > len(m_lis):
            print("MEMORY DELETED")
            return
        while True:
            if (len(j_lis) == idx_j) or (len(m_lis) == idx_m):
                break
            j_p = j_lis[idx_j]
            m_p = m_lis[idx_m]
            if (j_p == m_p):
                idx_j += 1
                idx_m += 1
            elif j_p != m_p:
                self.updateProblemList.append(m_p)
                idx_m += 1
    def copyFileToMemory(self, path):
        paste_folder_path = self.problemListPath
        token = path.split('/')
        shutil.copyfile(path, paste_folder_path + token[-1])
        print("COPY:",token[-1])
    def setDiffMemory(self, json_problem):
        json_problem = set(json_problem)
        memory_problem = set()
        for root, directories, files in os.walk("../problem_list"):
            for file in files:
                name, type = file.split('.')
                memory_problem.add(int(name))
        path = dict()
        for p, n in self.fileLists[0]:
            path[n] = p
        for problem in json_problem.difference(memory_problem):
            self.copyFileToMemory(path[problem])
    def updateProblemFolder(self):
        with open("problem_list.json", 'r') as db:
            j = json.load(db)
            j_total = j['baekjoon']['total']
            j_problems = j['baekjoon']['problems']
            m_total = len(self.problemList)
            m_problems = self.problemList
            if j_total < m_total:
                self.setUpdateFileList(j_problems, m_problems)
                print(self.updateProblemList)
                j['baekjoon']['total'] = m_total
                j['baekjoon']['problems'] = m_problems
                self.updateJson(j)
            self.setDiffMemory(j['baekjoon']['problems'])


if __name__ == '__main__':
    analyzer = Analyzer()
    fileList = analyzer.getFileList()
    print(analyzer.path)
    analyzer.updateProblemFolder()
    # TODO 이슈처리, 파일 타입, ...
    # analyzer.createJson()
    # analyzer.saveJson()
    # analyzer.fileCopyToFolder(fileList[0])