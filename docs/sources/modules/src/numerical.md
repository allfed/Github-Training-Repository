#


### bumpy_reduction
[source](https://github.com/allfed/My-Super-Cool-Respository/blob/master/src/numerical.py/#L1)
```python
.bumpy_reduction(
   x, recursions = 5
)
```

---
This function is a recursive function that does some whacky things that I can't explain

**Arguments**

* **x**  : input number
* **recursions**  : must be a positive int, default is 5 if noit specified, is the number of times the function will recurse


**Returns**

* **function**  : if recursions is 0, returns x, otherwise returns bumpy_reduction(x/2 + recursions**2, recursions - 1)

