#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints python's object
 * @p: pointer
 */

void print_python_list_info(PyObject *p)
{
unsigned int len = PyList_Size(p);
unsigned int allocated = ((PyListObject *) p)->allocated;
unsigned int l_idx = 0;

if (p == NULL)
return;

printf("[*] Size of the Python List = %u\n", len);
printf("[*] Allocated = %u\n", allocated);

while (l_idx < len)
{
PyTypeObject *type = PyList_GET_ITEM(p, l_idx)->ob_type;
const char *name = type->tp_name;
printf("Element %u: %s\n", l_idx, name);

l_idx++;
}
}

