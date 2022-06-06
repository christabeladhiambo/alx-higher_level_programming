#include <Python.h>
#include <stdio.h>

/**
* print_python_list_info - print info about the python
* Object
*
* @p: The python object
*/
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = 0, i, alloc;

    if(PyList_CheckExact(p))
    {
	size = ((PyVarObject *)p)->ob_size;
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %lu\n", size);
		printf("[*] Allocated = %lu\n", alloc);

	for (i = 0; i < size; i++)
	{
	    printf("Element %ld: %s\n", i, ((PyListObject *)p)->ob_item[i]->ob_type->tp_name);
	}
    }
}
