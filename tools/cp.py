
from shutil import copy

failedFiles = open("failed.txt").read().splitlines(False)
for file in failedFiles:
	copy(file, "failed/" + file)
