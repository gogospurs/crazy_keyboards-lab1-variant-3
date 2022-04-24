# crazy-keyboards - lab 1 - variant 3

Group Member:

- Haixiao Wang 212320012
- Yu Zhang     212320015

## Variant description

- set based on binary-tree,

and should check the implementation correctly works with None value.

## Project structure

- `binary_tree_mutable.py` -- implementation of `BinaryTree` mutable version

- `mutable_test.py` -- unit and PBT tests for mutable binary tree

## Features

- PBT: `test_toAndfrom_list`, `test_getSize`

- other test module: `test_findElem`, `test_add`, `test_delete`,

`test_filter`, `test_map`, `test_reduce`, `test_monoid`, `test_iter_next`

## Contribution

- Yu Zhang -- source part and upload the files to github
- Haixiao Wang -- test part

## Explanation of taken decision and analysis

- The libarary mainly contains two parts,

one is mutable object part,

and the function in it will change the source object.

## Conclusion

- First of all, in this lab,

we met many problems that need to be considered as a library developer.

An excellent container library should support functions of variable objects.

Function, which helped us detect many problems,

we also learned to use Hypothesis library to do the test.

## Changelog

- 14.04.2022 - 0
  - Initial

- 19.04.2022 - 1
  - fix some problem
    - rename test file from the mutable_test to binary_tree_mutable_test.
    - add PBT to some test module.
    - modify the mconcat function to mutable version, and modify correspondding test.
    - make sure the map function won't be the source of undifined behavior.
