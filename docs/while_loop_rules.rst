While Loop Rules
----------------

while_loop_001
##############

This rule checks for indentation of the **while** keyword.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

   while (temp /= 0) loop
       temp := temp/2;
     end loop;

**Fix**

.. code-block:: vhdl

   begin

     while (temp /= 0) loop
       temp := temp/2;
     end loop;


while_loop_002
##############

This rule checks for indentation of the **end loop** keyword.
The **end loop** must line up with the **while** keyword.
Proper indentation enhances comprehension.

**Violation**

.. code-block:: vhdl

   begin

     while (temp /= 0) loop
       temp := temp/2;
         end loop;

**Fix**

.. code-block:: vhdl

   begin

     while (temp /= 0) loop
       temp := temp/2;
     end loop;

