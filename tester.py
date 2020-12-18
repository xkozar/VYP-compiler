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

for testCase in testCases:
    resultFile = open(testCase + testResultSuffix, 'r')
    outputFile = open(testCase + testOutputSuffix, 'w')
    process = subprocess.Popen(['python', 'src/main.py', f'{testCase}{testSuffix}'], stdout=outputFile, stderr=outputFile)
    process.communicate()
    expectedReturnCode = int(resultFile.readline().strip())
    if process.returncode != expectedReturnCode:
        print("FAIL: test", testCase, "returned code is ", process.returncode, ", expected return code", expectedReturnCode)
        continue
    #print("PASS: test", testCase, "passed")


    outputFile.close()

    intOutputFile = open(testCase + testIntOutputSuffix, 'w')
    process2 = subprocess.Popen(['java', '-jar', 'vypint-1.0.jar', f'{testCase}{testOutputSuffix}'], stdout=intOutputFile, stderr=intOutputFile)
    interpretOutput = process2.communicate()
    intOutputFile.close()

    intOutputFile = open(testCase + testIntOutputSuffix, 'r')
    resultOutput = intOutputFile.readlines()
    refOutput = resultFile.readlines()
    intOutputFile.close()
    if process2.returncode != 0:
        print("FAIL: interpret: test", testCase, "returned code is ", process2.returncode)
        continue

    if resultOutput != refOutput:
        print("Result output for", testCase, "is different from referenced output")
        continue

    print("PASS: test", testCase, "passed")

    resultFile.close()
    outputFile.close()
