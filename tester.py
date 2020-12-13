from os import walk
import subprocess

testSuffix = '.test'
testResultSuffix = '.result'
testOutputSuffix = '.output'

allFileNames = []

for fileNames in walk("./tests"):
    for fileName in fileNames[2]:
        allFileNames.append(f'{fileNames[0]}\\{fileName}')

testFileNames = list(filter(lambda fileName: fileName.endswith(testSuffix), allFileNames))
testCases = list(map(lambda testCase: testCase.replace(testSuffix, ''), testFileNames))

for testCase in testCases:
    resultFile = open(testCase + testResultSuffix, 'r')
    outputFile = open(testCase + testOutputSuffix, 'w')
    process = subprocess.Popen(['python', 'src/main.py', f'{testCase}{testSuffix}'], stdout=outputFile)
    process.communicate()
    expectedReturnCode = int(resultFile.readline().strip())
    if process.returncode != expectedReturnCode:
        print("FAIL: test", testCase, "returned code is ", process.returncode, ", expected return code", expectedReturnCode)
        continue
    print("PASS: test", testCase, "passed")
    # process = subprocess.Popen(['java', '--jar', 'vypint-1.0.jar', outputFile])
    # interpretOutput = process.communicate()[0]

