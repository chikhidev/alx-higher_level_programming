#include "Python.h"
#include <stdio.h>
#include <float.h>

/**
* print_python_list - Prints information about a Python list object.
*
* @p: Pointer to a Python object.
*
* Return: void.
*/
void print_python_list(PyObject *p)
{
Py_ssize_t list_size;
Py_ssize_t idx;
PyObject *item;

printf("[*] Python list info\n");
if (PyList_Check(p))
{
list_size = PyList_Size(p);

printf("[*] Size of the Python List = %zd\n", list_size);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

for (idx = 0; idx < list_size; idx++)
{
item = PyList_GetItem(p, idx);
printf("Element %zd: %s\n", idx, Py_TYPE(item)->tp_name);

if (PyBytes_Check(item))
print_python_bytes(item);
else if (PyFloat_Check(item))
print_python_float(item);
}
}
else
printf("  [ERROR] Invalid List Object\n");

fflush(stdout);
}

/**
* print_python_bytes - Prints information about a Python bytes object.
*
* @p: Pointer to a Python object.
*
* Return: void.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t bytes_size;
Py_ssize_t idx;
Py_ssize_t max;
char *str;

printf("[.] bytes object info\n");
if (PyBytes_Check(p))
{
bytes_size = PyBytes_Size(p);
str = PyBytes_AsString(p);
printf("  size: %zd\n  trying string: %s\n", bytes_size, str);

if (bytes_size < 10)
max = bytes_size + 1;
else
max = 10;

printf("  first %zd bytes: ", max);
for (idx = 0; idx < max - 1; idx++)
printf("%02x ", (unsigned char)str[idx]);
printf("%02x\n", (unsigned char)str[max - 1]);
}
else
printf("  [ERROR] Invalid Bytes Object\n");

fflush(stdout);
}

/**
* print_python_float - Prints information about a Python float object.
*
* @p: Pointer to a Python object.
*
* Return: void.
*/
void print_python_float(PyObject *p)
{
double value;

printf("[.] float object info\n");
if (PyFloat_Check(p))
{
value = PyFloat_AsDouble(p);

printf("  value: %f\n", value);
}
else
printf("  [ERROR] Invalid Float Object\n");

fflush(stdout);
}
