# Test Builder Application

This application serves as generator of unique tests for course students.
The application allows lector to provide sets of questions organized into groups by
topic or difficulty and specify number of questions from each group which ought to be
in the tests. Based on this input, unique tests are generated for each
of the student.

## Configuration

This section governs necessary steps to create valid configuration.

For initial configuration copy the `testbuilder/cfg-example.py` as
`testbuilder/cfg.py` and adjust its values as needed.

### Test Data

This section describes how-to create test data. For initial collection,
copy the `testbuilder/data-example.py` as `testbuilder/data.py`.

TBD

## Run and output

To run the program, run the following outside of the testbuilder folder:

```
python -m testbuilder.builder
```

Output will be found in `output.txt` file by default. With default
configuration the contents of the whole file can be copied to a text processor
and printed to A4 pages without any additional changes.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Exam Builder</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/danekja/exam-builder" property="cc:attributionName" rel="cc:attributionURL">Jakub Danek</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.