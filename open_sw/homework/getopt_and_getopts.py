쉘스크립트를 사용할 때 사용자가 입력을 받는 경우가 있다. 
값을 입력받고 옵션을 구현하는  방법이 있다.
그 입력을 받는 방법중 getopt와 getopts에 대해 알아보았다.

먼저 getopt와 getopts의 장점은
1. 다양한 값을 입력 받을 경우 편의를 위해서
2. 스크립트를 체계적으로 관리 할 수 있다. 
3. 옵션을 구현하기에 편리하고 간단하다. 

예를들어 

// while getopt "a:b" option
do 
 case $option in
 a)
    echo "이 옵션은 a입니다 " 
   ;;

 b)
    echo "이 옵션은 b입니다 " 
  ;; 
esac

done

이 처럼 a 옵션과 b 옵션을 넣는 경우이다.

만약 b의 내용을 수정하여 
arg_b =$OPTARG 를 추가한다면 값을 OPTARG 변수에 저장하게 된다. 


getopt의 주의해야 하는 점은 getopt는 한개의 문자만을 구분자로 사용한다는 점이다. 



