(module
  ;; function printf (imported): int, int -> void
  (import "c4wa" "printf" (func $printf (param i32) (param i32)))
  ;; memory (exported)
  (memory (export "memory") 1)
  ;; "%d + %d = %d\n" is written at address 1024
  (data (i32.const 1024) "%d + %d = %d\0A\00")
  ;; function add (exported): int, int -> void
  (func $add (export "add") (param $a i32) (param $b i32)
    ;; memory[0-7] = $a
    (i64.store (i32.const 0) (i64.extend_i32_s (get_local $a)))
    ;; memory[8-15] = $b
    (i64.store (i32.const 8) (i64.extend_i32_s (get_local $b)))
    ;; memory[16-23] = $a + $b
    (i64.store (i32.const 16) (i64.extend_i32_s (i32.add (get_local $a) (get_local $b))))
    ;; printf(1024, 0)
    (call $printf (i32.const 1024) (i32.const 0))))
