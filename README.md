# uf-transcript2csv

Python CLI tool that exports data from the ONE.UF unofficial transcript webpage in a CSV format.

Currently only works for undergraduate tracks.

## Requirements

- `pandas`

## Usage Instructions

1. Download JSON data
    1. Open [https://one.uf.edu/transcript/](https://one.uf.edu/transcript/) and login if needed
    2. Run these commands in the browser console

    		div = $('[ng-repeat="record in $ctrl.unofficialTranscript.records track by $index"]')
    		scope = angular.element(div).scope()
    		console.log(JSON.stringify(scope.$ctrl.unofficialTranscript.records))

    3. Copy/paste the output string into a file (ex. `records.json`)
2. Run command

		$ python uf-transcript2csv.py <records.json> <records.csv>
3. Open CSV file in your favorite table editor and do your calculations!
