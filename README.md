# ONE.UF Unofficial Transcript GPA Calculator

Python CLI tool for calculating overall GPA and major GPA from ONE.UF unofficial transcript webpage.

## Usage Instructions

1. Download JSON data
    1. Open [https://one.uf.edu/transcript/](https://one.uf.edu/transcript/) and login if needed
    2. Run these commands in the browser console

    		div = $('[ng-repeat="record in $ctrl.unofficialTranscript.records track by $index"]')
    		scope = angular.element(div).scope()
    		console.log(JSON.stringify(scope.$ctrl.unofficialTranscript.records))

    3. Copy/paste the output string into a file (ex. `records.json`)
2. Change `major_prefixes` in `oneuf_gpa.py`
3. Run command

		$ python oneuf_gpa.py -i <records.json>
		...
		...
		Overall GPA: <YOUR OVERALL GPA>
		Major GPA: <YOUR MAJOR GPA>
