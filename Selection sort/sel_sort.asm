.data 
  n: .word 7
  arr: .word -2,2,5,1,4,3,-1
.text
  main:
    lw $s1, n #$s1=n
    li $s2, 0 #$s2=i=0
    subi $t0, $s1, 1
    loop:
      slt $t1, $s2, $t0
      beq $t1, $zero, exit
      add $s4, $s2, $zero #$s4=minindex=i
      addi $s5, $s2, 1 #s5=j=i+1
      loop1:
        slt $t1,$s5, $s1 #if(j<n)
        beq $t1, $zero, exit1
        sll $t3, $s5, 2
        sll $t4, $s4, 2
        lw $t3, arr($t3) #$t3=arr[j]
        lw $t4, arr($t4) #$t4=arr[minindex]
        slt $t1, $t3, $t4 #arr[j]<arr[minindex]
        beq $t1, $zero, end1 #if not then go to end1
        add $s4, $s5, $zero #minindex=j
        end1: 
          addi $s5, $s5, 1 #j++
          j loop1
      exit1:
        beq $s4, $s2, end #if(minindex!=i)
        sll $t3, $s4, 2 #$t3=minindex*4
        sll $t4, $s2, 2 #t4=i*4
        lw $t5, arr($t3) #$t5=arr[minindex]
        lw $t6, arr($t4) #$t6=arr[i]
        sw $t5, arr($t4) #arr[i]=$t5
        sw $t6, arr($t3) #arr[minindex]=$t6
        end:
          addi $s2, $s2, 1 #i++
          j loop
  exit:
          
          
          
          
      
