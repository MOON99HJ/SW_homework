# 20182298 문희중 오픈소스SW homework

>## ● 목차
>### ● getopt & getopts 명령어
>### ● sed 명령어
>### ● awk 명령어 
>
>
><img src="https://user-images.githubusercontent.com/94624031/142752262-4263e28e-9d67-42e9-bd3e-24d5fa09ee01.jpg" width="250" height="210">






# ● getopt & getopts 명령어

>쉘스크립트를 사용할 때 사용자가 입력을 받는 경우가 많이 발생하게 된다           
>일반적인 값을 입력받는 것에 그치지 않고 옵션을 추가하여 구현하여 방법들이 존재한다           
>옵션을 받아 입력받는 방식의 입력을 받는 방법중 getopt와 getopts에 대하여 알아보았다.          

### ○ **getopt와 getopts의 사용하는 이유는 무엇일까?**
|1 |다양한 값을 입력 받을 경우 편의를 제공한다.|
|---|----------|
|2 |옵션을 구현하기에 편의를 제공한다.|
|3 |스크립트를 체계적으로 관리 할 수 있게 된다.|

> ### ○ **getopt와 getopts의 차이점은 무엇인가?**
> |getopt|긴 변수 이름을 사용하고 싶을때, 변수 이름이 하나만 있을때|
> |---|---------------|
> |getopts|모든 posix 쉘에서 작동한다, 옵션종결자로 '-'를 이해한다|
> 
> 그렇다면 getopts로 긴 옵션을 사용하기 원한다면?          
> 대시문자와 콜론을 OPTSPEC에 넣어 사용하면 된다!!          


>  #### ● **알아보기**
> > ##### 먼저 예시를 알아보자          
> > 1) getopt 명령을 줄 때 사용자가 처리하고자 하는 인자를 입력한다.          
> > 2) a 옵션의 경우는 인수를 받지 않은다.          
> > 3) p 옵션의 경우는 인수를 받는다.          
> > 4) 인수를 받기를 원할때는 OPTARG 라는 쉘 변수를 이용한다.          
> > ```
> > #!/bin/sh
> > box = 0
> > separator = ""
> > while getopts "ap:' option
> > do
> >  case $option in
> >    a)
> >      box =1
> >      ;;
> >    p) 
> >      separator="$OPTARG"
> >      ;;
> >    \?)
> >      echo "Usage: getopts.sh [-a] [-p separator] target_dir" 1>&2 
> >      exit 1
> >      ;;
> >    esac
> >  done
> >  shift $(expr $OPTIND-1)
> >  path = '$1"
> >  ```
> >  OPTIND는 getopt 처리하고 남은 다음 처리할 인덱스 번호가 된다.        
> >  shitf 명령은 명령행 인자중에 삭제할 인자 개수를 지정한다. 
> 
> > #### ● **short 옵션**
> > 위의 예시를 보면 알수있듯 쉘에서는 명령을 실행할 때 옵션을 사용한다.        
> > 옵션 해석 작업을 쉽게 도와주는 것이 getopts이다.        
> > getopts는 옵션 short와 long중 short 옵션을 처리하기에 short에 대해 알아보았다.        
> > ```
> > $ command -a -b -c
> > ```
> > 예시처럼 옵션을 붙여서 사용이 가능하며 순서가 바뀌어도 상관없다.
> > ```
> > $ command -abc
> > $ command -b -ca
> > ```
> > 옵션의 인수를 가질 수 있다.
> > ```
> > $ command -a xxx -b -c yyy
> > ```
> > 옵션인수를 옵션에 붙여 사용 할 수 있다.
> > ```
> > $ command -axxx -bcyyy
> > ```
> > '--' 옵션 구분자가 올 경우 우측에 있는 값은 옵션으로 해석하면 안된다.
> > ```
> > $ command -a -b -- -c
> > ```
> 
> >  #### ● **getopt 결과**
> >  getopt가 처리가 완료된다면 option를 리턴하게 된다.           
> >  option-argument가 존재하면 optarg에 설정한다.         
> >  에러가 발생하면 '?'을 리턴한다.         
> >  
> >  #### ● **Error 발생의 원인**
> >  '-'로 시작하는 문자열이지만 option character가 없는 경우         
> >  option-argument를 갖는 option이지만 option-character가 없는 경우         
> >  또한 다음으로 처리할 option이 없어진 경우 -1을 리턴한다.         
        


# ● sed 명령어
> sed 명령어란? Stream Editor 의 줄임말이다.          
> 명령어로 원본 텍스트 파일을 편집해주는 명령어이다.


### ● sed 기본 형태 
> sed를 사용할 경우 pattern buffer의 내용을 자동으로 출력하게 된다.          
> 이때 sed 뒤에 -n을 붙이며 사용하게 되면 pattern buffer의 내용을 출력하지 않게된다.         
> 따라서 sed -n이 기본적인 형태라고 보면 된다

### ● -e 옵션
> -e 를 추가하여 사용자가 사용할 커맨드를 이용하여 텍스트 파일을 가공해준다.          
> > #### ● **특정 행 출력하기**
> > 1,$p 이나 /$/p 를 사용하면 출력이 가능하다.
> > ``` 
> > sed -n -e '/$/p' 특정파일
> > sed -n -e '1,$p' 특정파일
> > ```
> > 원하는 구간 출력도 가능하다
> > (1번째 줄부터 6번째 줄까지 출력한다면)
> > ```
> > sed -n -e '1,6p' 특정파일
> > ```
> > 다중으로도 사용 가능하다. (1번째 줄과 4번째줄 부터 6번째 줄까지)
> > ```
> > sed -n -e '1p' -e '4,6p' 특정파일
> > ```
> 
> >#### ● **특정 행 삭제하기**
> > 3 ~ 5번째 줄을 삭제하고 출력
> > ```
> > sed -n -e '3,5d' -e '1,$p' 특정파일
> > ```
> 
> > #### ● **특정 단어 변경하기**
> > 특정한 단어를 원하는 단어로 변경 가능하다
> > ```
> > s/before/after/g (before은 변경 문자열 ,after은 변경 후 문자열이다.)
> > ```
>  
> > #### ● **문자열 추가하기**
> > 사용자가 원하는 문자열을 위치에 추가할 수 있다.
> > ```
> > /찾을 문자열/i\위에 삽입할 문자열
> > /찾을 문자열/a\다음 줄에 추가할 문자열
> > ```
> 
> > #### ● **내용 교체하기**
> > 해당 기능을 사용시 행의 내용이 전부 교체된다. 
> > ```
> > /교체하고 싶은 내용을 포함한 문자열/c\교체 내용
> > sed -n -e/교체하고 싶은 내용을 포함한 문자열/c\교체 내용
> > ```
> 
> > #### ● **특정 행에 파일 내용을 추가하기**
> > 특정 파일의 내용을 추가할 수 있다.
> > ```
> > sed -n -e '특정 내용 파일' -e '원래파일'

# ● awk 명령어
> ### awk 명령어란?        
> sed 명령어와 달리 명령어를 개발한 사람들의 이름을 약자로 만든 명령어이다.         
> 유닉스에서 개발된 스크립트 언어이다.        
> 텍스트가 입력되어 있는 파일을 가공하거나 원하는 내용으로 필터링하며 추가한 결과를 행과 열로 출력해준다.

# ● awk 예시 파일
> awk 명령어의 예시 이해를 돕기위해 간단한 파일을 제작하였다.         
> 어느한 학교의 학생부 명단 파일이다.         
> 이름은 학생부.txt 로 지정하겠다.          
> |name|birth|phone|sex|grade|
> |---|--------|--------|---|---|
> |Kim|1999-02-17|010-5050-1122|M|1|
> |Moon|1998-01-15|010-2035-5566|W|2|
> |Park|1999-05-22|010-7454-9969|W|4|
> |Oh|1995-09-14|010-8445-0012|M|2|
> |Hong|1996-11-11|010-1110-7470|M|3|
>          
>          
> > #### ● **열 출력하기**
> > $는 열에 대응한다. 이를 이용하면
> > ```
> > awk '{ print $1 }' ./학생부.txt
> > ```
> > ```
> > name
> > Kim
> > Moon
> > Park
> > Oh
> > Hong
> > ```
> > ```
> > awk '{ print $1,$4 }' ./학생부.txt
> > ```
> > ```
> > name sex
> > Kim M
> > Moon W
> > Park W
> > Oh M
> > Hong M
> > ```
> 
> > #### ● **특정 포함된 출력**
> > 사용자가 원하는 문자열이 포함된 부분을 출력 할 수도 있다.
> > ```
> > awk `/Moon/' ./학생부.txt
> > ```
> > ```
> > Moon 1998-01-15 010-2035-5566 W 2
> > ```
> 
> > #### ● **출력에 내용 첨가하기**
> > 원하는 내용을 첨가하여 출력이 가능하다
> > ```
> > awk '{ print ("name : " $1, ", "  "birth : " $2) }' ./학생부.txt
> > ```
> > ```
> > name : name, birth : birth
> > name : Kim , birth : 1999-02-17
> > name : Moon, birth : 1998-01-15
> > name : Park, birth : 1999-05-22
> > name : Oh, birth : 1995-09-14
> > name : Hong, birth : 1996-11-11
> > ```
> 
> >  #### ● **특정 내용 검색하기**
> >  파일에서 특정 내용을 검색하여 출력 할 수 있다.         
> >  사용방법은 흔히 여러 언어에서 사용하는 if문을 사용한다.         
> >  ```
> >  awk '{ if ( $5 == 2 ) print ($0) }' ./학생부.txt
> >  ```
> >  이와 같이 입력하게 되면 학년이 2학년인 학생들만 출력이 가능하다.
> >  ```
> >  name birth phone sex grade
> >  Moon 1998-01-15 010-2035-5566 W 2
> >  Oh 1995-09-14 010-8445-0012 M 2
> >  ```
> >  
> >  여러 조건을 추가하여 사용도 가능하다.
> >  ```
> >  awk '{ if ( $4 == "M" && $5 == 3) print ($0) }' ./학생부.txt
> >  ```
> >  ```
> >  Hong 1996-11-11 010-1110-7470 M 3
> >  ```
> >  
