'''
    project: VYPlanguage compiler
    file: code_generator.py
    authros: Maroš Holko, xholko01
'''

from os import walk
import subprocess

testSuffix = '.test'
testResultSuffix = '.result'
testOutputSuffix = '.output'
testIntOutputSuffix = '.int'

allFileNames = []

for fileNames in walk("./tests"):
    for fileName in fileNames[2]:
        allFileNames.append(f'{fileNames[0]}\\{fileName}')
        #allFileNames.append(f'{fileNames[0]}/{fileName}')    # merlin

testFileNames = list(filter(lambda fileName: fileName.endswith(testSuffix), allFileNames))
testCases = list(map(lambda testCase: testCase.replace(testSuffix, ''), testFileNames))

passed = 0
failed = 0

for testCase in testCases:
    compilationOK = True
    resultFile = open(testCase + testResultSuffix, 'r')
    outputFile = open(testCase + testOutputSuffix, 'w')
    process = subprocess.Popen(['./vypcomp.sh', 'src/main.py', f'{testCase}{testSuffix}'], stdout=outputFile, stderr=outputFile)
    process.communicate()
    expectedReturnCode = int(resultFile.readline().strip())
    if process.returncode != expectedReturnCode:
        print("FAIL: test", testCase, "returned code is ", process.returncode, ", expected return code", expectedReturnCode)
        failed += 1
        compilationOK = False

    if compilationOK and (expectedReturnCode != 0):
        passed += 1
        print("PASS: test", testCase, "passed")

    outputFile.close()
    resultFile.close()

    interpretOK = True
    if compilationOK and (expectedReturnCode == 0):
        intOutputFile = open(testCase + testIntOutputSuffix, 'w')
        process2 = subprocess.Popen(['java', '-jar', 'vypint-1.0.jar', f'{testCase}{testOutputSuffix}'], stdout=intOutputFile, stderr=intOutputFile)
        interpretOutput = process2.communicate()
        intOutputFile.close()

        resultFile = open(testCase + testResultSuffix, 'r')
        resultFile.readline()
        refOutput = resultFile.readlines()
        intOutputFile = open(testCase + testIntOutputSuffix, 'r')
        resultOutput = intOutputFile.readlines()

        if process2.returncode != 0:
            failed += 1
            print("FAIL: interpret: test", testCase, "returned code is ", process2.returncode)
            interpretOK = False

        if interpretOK:
            if resultOutput != refOutput:
                failed += 1
                print("FAIL: Result output for", testCase, "is different from referenced output")
                interpretOK = False

        if interpretOK:
            passed += 1
            print("PASS: test", testCase, "passed")

        resultFile.close()
        intOutputFile.close()


print("Total tests: ", len(testCases), "Passed: ", passed, "Failed: ", failed, "\n")
