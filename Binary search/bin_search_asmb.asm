.data
  n: .word 7
  arr: .word 1, 5, 7, 10, 13, 18, 22  
  ele: .word 13                       #val to search
  res: .word -1
.text
main: 
  li $s1, 0 #$s1=l=0
  lw $s2, n  #$s2=n
  subi $s3, $s2, 1 #$s3=r=n-1
  loop:
    bgt $s1,$s3,exit #if l>r exit out of loop
    add $t0,$s1,$s3 #$s1+$s3
    srl $s4, $t0, 1 #mid=(l+r)/2
    sll $t0, $s4, 2 #mid*4
    lw $t2, arr($t0) #t2=arr[mid]
    lw $t3, ele #t3=ele
    bne $t2, $t3, next #if(arr[mid]!=ele) go to next
    add $s5,$s4,$zero #s5=mid
    sw $s5, res #res=mid
    j exit
    next:
      slt $t4, $t2, $t3 #if(arr[mid]<ele)
      beq $t4, $zero, next1 #if condition is false go to next1
      addi $s1, $s4,1 #l=mid+1
      j end
    next1:
      slt $t4, $t3, $t2 #if(arr[mid]>ele)
      beq $t4, $zero, end #if condition is false go to end
      subi $s3,$s4,1 #r=mid-1
    end:
      j loop
  exit:
    
    
  
  
