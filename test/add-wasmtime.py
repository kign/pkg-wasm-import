#! /usr/bin/env python3
# python3 -m pip install --upgrade wasmtime
import sys
from wasm_import import sprintf

def main (num1 : int, num2 : int) :
    from wasmtime import Store, Module, Instance, Func, FuncType, ValType
    store = Store()

    module = Module.from_file(store.engine, "add.wat")

    def printf(p_fmt, offset):
        mem = instance.exports(store)["memory"].data_ptr(store)
        res = sprintf(p_fmt, mem, offset)
        print(res, end='')

    instance = Instance(store, module, [Func(store, FuncType([ValType.i32(), ValType.i32()], []), printf)])
    instance.exports(store)["add"](store, num1, num2)


if __name__ == "__main__" :
    if len(sys.argv) != 3 :
        print(f"USAGE: {sys.argv[0]} <num 1> <num 2>")
        exit(0)
    main(int(sys.argv[1]), int(sys.argv[2]))