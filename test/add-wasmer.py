#! /usr/bin/env python3
# python3 -m pip install --upgrade wasmer wasmer_compiler_llvm
import sys
from wasm_import import sprintf

def main (num1 : int, num2 : int) :
    from wasmer import engine, Store, Module, Instance, Function, FunctionType, Type, ImportObject
    from wasmer_compiler_llvm import Compiler
    store = Store(engine.Native(Compiler))

    module = Module(store, open("add.wat", 'r').read())
    import_object : ImportObject = ImportObject()

    def printf(p_fmt, offset):
        mem = instance.exports.memory.uint8_view()
        res = sprintf(p_fmt, mem, offset)
        print(res, end='')

    import_object.register("c4wa", {"printf" : Function(store, printf,
                                    FunctionType(params=[Type.I32, Type.I32], results=[]))})

    instance = Instance(module, import_object)
    instance.exports.add(num1, num2)


if __name__ == "__main__" :
    if len(sys.argv) != 3 :
        print(f"USAGE: {sys.argv[0]} <num 1> <num 2>")
        exit(0)
    main(int(sys.argv[1]), int(sys.argv[2]))