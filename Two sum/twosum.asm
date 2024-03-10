.data
  n: .word 7
  arr: .word 1, 5, 7, 10, 13, 18, 22
  x: .word 18
  res: .word 0
.text
  li $s0, 0 #$s0=l=0
  lw $s1, n #$s1=n
  subi $s2, $s1, 1 #$s2=r=n-1
  lw $s3, x #$s3=x
  loop:
    bgt $s0, $s2, exit #if l>r exit
    sll $t0, $s0, 2 #$t0=l*4
    sll $t1, $s2, 2 #$t1=r*4
    lw $t0, arr($t0) #$t0=arr[l]
    lw $t1, arr($t1) #$t1=arr[r]
    add $t2, $t0, $t1 #$t2=arr[l]+arr[r]
    bne $t2, $s3, next #if(arr[l]+arr[r]!=x) go to next
    li $t3, 1 #$t3=1
    sw $t3, res #res=$t3=1
    j exit
    next:
      bgt $t2, $s3, next1 #if(arr[l]+arr[r]>x) go to next
      addi $s0, $s0, 1 #l++
      j loop
    next1:
      subi $s2, $s2, 1 #r--
      j loop
  exit:
      
      
    
