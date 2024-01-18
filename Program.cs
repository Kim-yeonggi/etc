//using System;   // 네임스페이스에 대한 선언부
using System.Runtime.InteropServices;
using System.Security.Cryptography.X509Certificates;
using static System.Console;
using static System.Math;

namespace Helloworld    // 네임스페이스 지정
{
    enum Level
    {
        High,
        Normar,
        Low
    }

    enum Align
    {
        Top,
        Bottom,
        Left=4,
        Right,
    }

    class Program   // 클래스명 지정
    {
        struct Student
        {
            public string name;
            public int kor;
            public int eng;
            public int math;
        }

        struct Point    // 구조체 이름 선언
        {
            public int x;   // 구조체 내부에 선언된 변수
            public int y;
        }
        
        struct Profile
        {
            public string Name;
            public int Age;
        }

        // 오버로드 : Main() 함수 바깥에 있어야 가능
        static void GetNum(int number)
        {
            Console.WriteLine(number);
        }
        static void GetNum(long number)
        {
            Console.WriteLine(number);
        }

        static int myabs(int x)
        {   
            return (x<0 ? -x : x);
        }

        static int intFunc(int x)
        {
            int result = x * 100;
            return result;
        }

        static string GetString()   // void : 리턴 X / void 자리에 반환값의 자료형 입력
        {
            return "반환값";
        }
        
        static void ShowMessage(string message)
        {
            Console.WriteLine(message);
        }
        static void myfunc()        // 매개변수, 반환 X
        {
            Console.WriteLine("함수실행");
        }

        static void Main()  // 함수 선언
        {
            /*
            //Console.WriteLine("Hello World");   // 실행문
            WriteLine("Hello World");

            // 소스코드의 컴파일
            // c# 파일은 program.cs 처럼 확장자가 cs 임
            // 컴파일 과정을 커치면 실행 가능한 exe 파일이 생성
            // 윈도우가 아닌 환경이면 dll을 생성
            // c# : 컴파일 방식 (빌드를 통해 컴파일)
            // 1.소스코드 작성    2. 빌드   3.프로그램 실행
            // 네임스페이스.클래스.메서드()
            // Main() 메서드의 의미
            // : C# 기본 구조에서 반드시 사용되는 Main() 메서드는 프로그램의 시작점을 의미
            // : 반드시 Main() 메서드가 있어야 함
            // : Main() 메서드에서 프로그램을 시작하고 종료한다.
            // Main() 메서드가 2개면 프로그램 진입점이 2개라는 의미 -> 오류 발생
            // Main 대소문자 구분
            // System도 대문자로 시작
            // 실행 단축키 : Ctrl + F5

            Console.WriteLine("줄바꿈");    // 자동 줄바꿈
            Console.Write("바꿈 X");        // 줄바꿈 X
            Console.Write("바꿈 X");        // 줄바꿈 X
            // 이스케이프 코드 or 이스케이프 시퀀스
            // \n  \t  \'  \"

            // 문자열 포매팅
            Console.WriteLine("{0}", "Hello");
            Console.WriteLine("{1} {0}", "Hello", "World");

            // 변수
            // C# 에서 자주 사용하는 데이터 형식
            // int : 정수형 데이터
            // long : 큰 정수형 데이터
            // string : 문자열
            // bool : 불 타입
            // double : 실수형 데이터
            // object : C#에서 사용하는 모든 데이터 형식을 담을 수 있음.

            
            // 식별자 규칙
            // 첫글자는 문자로, 숫자X, 길이는 255 이하, 공백포함 불가, 키워드 사용 불가, 대소문자 구분
            int number;
            number = 0;
            Console.WriteLine(number);


            // 리터럴 사용
            // 변수에는 직접 정수형 또는 문자열 값 저장 가능
            // 리터럴이란 : 값 자체를 의미
            // 널 리터럴 : null 리터럴 : 값을 가지지 않는 리터럴
            Console.WriteLine(1234);    // 정수 리터럴
            Console.WriteLine(3.14F);   // 실수 리터럴
            Console.WriteLine(3.14L);   // long 리터럴
            Console.WriteLine('A');     // 문자 리터럴 ''
            Console.WriteLine("helloooooooooo");    // 문자열 리터럴 ""

            int num2 = 100;     // 변수 선언, 초기화 동시에 가능
            Console.WriteLine(num2); ;


            // 형식이 같은 변수 여러 개 동시 선언
            // 데이터 형식 변수1, 변수2, 변수3
            int num_1, num_2, num_3;
            num_1 = 100;
            num_2 = 200;
            num_3 = 300;
            Console.WriteLine("{0}{1}{2}",num_1,num_2,num_3);

            num_1 = num_2 = num_3 = 500;    // 변수 여러 개를 같은 값으로 한 번에 초기화 가능
            Console.WriteLine("{0}{1}{2}",num_1,num_2,num_3);

            // MyNum : 파스칼 표기
            // myNum : 캐멀 표기법
            // my_num : 스네이크 표기법

            // 변수 <-> 상수
            // 변수 : 변할 수 있는 값
            // 상수 : 고정 값
            // constant : const 키워드 사용
            const int MAX = 20;
            Console.WriteLine(MAX);
            // a = 30;  // error : 정수형 상수로 선언되어 있어서 값을 바꿀 수 없음.



            // 숫자 데이터
            // 정수 _ 실수
            // 부호가 있는 정수 _ 부호가 없는 정수
            // 부호가 있는: signed : + - 보호가 있는 정수형 => 음수 양수 표현 가능
            // 부호가 없는: unsigned : 부호없이 +만 다루는 정수형 데이터 타입
            // int 형식 = System.Int32 와 같다
            // 변수 선언시 int 대신 System.int32로 선언 가능
            // using System을 해놓은 상태라면, Systemp 생략하고 Int32로 선언 가능
            // 닷넷 형식 : System.Int32
            // 데이터 형식 : int 
            
            // 부호가 있는 정수 ( +  - )
            // 1. sbyte : System.SByte
            // 2. short : System.Int16
            // 3. int : System.Int32
            // 3. long : System.Int64

            // 부호가 없는 정수 (+)
            // 1. byte : System.Byte
            // 2. ushort : System.UInt16
            // 3. uint : System.UInt32
            // 2. ulong : System.UInt64

            int min = -2147483648;
            int max = +2147483647;
            Console.WriteLine(min);
            Console.WriteLine(max);

            Console.WriteLine("32비트 int 최소 : {0}", int.MinValue);
            Console.WriteLine("32비트 int 최대 : {0}", int.MaxValue);
            Console.WriteLine("64비트 long 최대 : {0}", long.MaxValue);
            Console.WriteLine("64비트 long 최소 : {0}", ulong.MaxValue);

            float f = 3.14F;
            double d = 3.140D;
            decimal m = 3.14M;
            Console.WriteLine("{0}{1}{2}",f,d,m);

            string msg = "hellooooo";
            Console.WriteLine($"{msg}");

            // 문자데이터 형식 char
            // 숫자 외의 데이터 형식(bool. char, string 등)
            // C#에서는 문자와 문자열을 구분
            // 문자는 char로 데이터 타입 정의
            // 문자는 2바이트 공간에 문자 하나를 저장한다.
            // 문자는 데이터 선언에 작은 따옴표 '' 사용
            // char c = 'c' 형태
            char c = 'c';
            Console.WriteLine(c);
            // 2바이트는 16비트 저장공간을 의미
            // char 키워드로 선언되는 변수는 단일 유니코드 문자 저장
            // 영문 및 한글 등 모든 언어 문자 표현 가능
            // 단일 캐릭터 char 데이터 타입에는 문자 여러개 저장 불가
            // 닷넷 형식으로는 System.Char로 표현한다.
            System.Char cc = 'a';
            Console.WriteLine(cc);
            char kor = '가';
            char grade = 'A';
            Console.WriteLine(kor);
            Console.WriteLine(grade);
            // char 타입 변수에 문자를 하나 이상 지정할 경우
            // 문자 리터럴에 문자가 너무 많다는 오류 발생   // ex) char x = 'abc';


            // 문자열 데이터 형식 string
            // 문자열을 반드시 큰 따옴표 "" 로 묶음
            // 낫넷 형식으로는 System.String
            string name = "kim";
            System.String name2 = "Lee";
            Console.WriteLine(name);
            Console.WriteLine(name2);

            // 문자열 보간법
            Console.WriteLine($"{name} {name2}");

            // string.Format() 함수 사용
            String msg1 = string.Format("{0} {1}","아","어");
            Console.WriteLine(msg1);

            String msg2 = "String";
            Console.WriteLine("Message: {0}", msg2);
            Console.WriteLine("Message: " + msg2);  // 더하기 연산
            Console.WriteLine($"Message: {msg2}");  // 보간법

            // bool
            // true false

            bool bln = true;
            bool bln2 = false;
            Console.WriteLine(bln);
            Console.WriteLine(bln2);

            Char ccc = 'A';
            Console.WriteLine(ccc);

            Console.ReadLine(); // 입력대기  input 과 동일
            Console.WriteLine(Console.ReadLine());  // print(input())
            
            Console.Write("이름을 입력하세요");
            string namex = Console.ReadLine();
            Console.WriteLine("{0}을 입력함", namex);


            // Console.Read() 메서드를 사용하면 콘솔에서 문자를 하나만 입력받을 수 있다.
            // 입력값은 문자에 해당하는 정수로 반환된다. -> 변환 필요
            // Convert.ToChar() 메서드를 사용해서 변환
            int aaa = Console.Read();                   // A 입력
            Console.WriteLine(aaa);                     // 65 출력
            Console.WriteLine(Convert.ToChar(aaa));     // A 출력

            // 형식 변환
            // Console.ReadLine() 메서드를 통해 콘솔에서 입력받은 데이터는 문자열
            // ReadLine()으로 입력받은 문자열을 형 변환

            // 1. 명시적 형변환
            // 2. 암시적 형변환

            // 암시적 형 변환은 변환 형식이 안전하게 유지되고 데이터가 손실되지 않는다.

            int x1 = 123;
            long x2 = x1;       // 암시적 형변환 예

            long x3 = 123;
            //int x4 = x3;      // 비트수 long > int => 에러 발생
            int x4 = (int)x3;   // 명시적 형변환
            // 형변환 : 캐스팅
            // 이 경우에서 (int)하지 않으면 데이터 손실 발생 오류


            // Convert 클래스의 주요 메서드  : 명시적 형변환
            // 1. ToString()    : 숫자 데이터 형식을 문자열로 변환
            // 2. ToInt32()     : 정수 형식으로 변환
            // 3. ToDouble()    : 실수 형식으로 변환
            // 4. ToChar()      : 문자 형식으로 변환
            // ex) Convert.ToString();


            // int.Parse() (명시적)형변환
            string strnum = "1234";
            int y = int.Parse(strnum);
            Console.WriteLine(y);


            // TryParse 메서드
            string strA = "10";
            string strB = "12.345";
            string strC = null;

            int i;
            Int32.TryParse(strA, out i);	// true (123)
            Int32.TryParse(strB, out i);	// false (0)
            Int32.TryParse(strC, out i);	// false (0)


            // GetType() 메서드
            int i = 1234;
            string ii = "안녕";
            char iii = 'c';
            double iiii = 3.14;
            Console.WriteLine(i.GetType());
            Console.WriteLine(ii.GetType());
            Console.WriteLine(iii.GetType());
            Console.WriteLine(iiii.GetType());
            // 파이썬 type() 메서드 비슷하게 활용
            // 데이터 타입 확인 메서드


            // 이진수 다루기
            Console.WriteLine(Convert.ToString(10, 2)); // 10진수 10을 2진수로 변환
            // 이진수 표현 1010
            
            Console.WriteLine(Convert.ToString(10, 2).PadLeft(8, '0'));
            // 8칸 기준으로 이진수 문자열 출력, 앞부분 0으로 채움


            // 바이트 선언
            byte b1 = 0b0010;
            byte x = 0x1f;
            Console.WriteLine(b1);  // 십진수 2 출력
            Console.WriteLine(x);  // 십진수 31 출력
            // 소스코드에서는 기본적으로 십진수 단위로 자료가 처리된다.


            int bin = 0b0001_0001;  // 4자리씩 _
            Console.WriteLine(bin); // 17

            int dec = 1_000_000;    // 3자리씩 _
            Console.WriteLine(dec);

            int hex = 0xA0_B0_C0;   // 2자리씩 _
            Console.WriteLine(hex);

            // var 키워드로 암시적 형식의 변수 생성
            var num100 = 100;
            Console.WriteLine(num100);
            var strrrr = "hello";
            Console.WriteLine(strrrr);
            Console.WriteLine(num100.GetType());    // System.Int32
            */

            /*
            // ReadKey() 메서드
            // 키보드에서 입력한 키를 알아내는 키워드
            Console.WriteLine("키보드 입력");
            ConsoleKeyInfo cki = Console.ReadKey(true);
            Console.WriteLine(cki.Key);
            Console.WriteLine(cki.KeyChar);
            Console.WriteLine(cki.Modifiers);
            if (cki.Key == ConsoleKey.Q)
            {
                Console.WriteLine("Q를 눌렀다.");
            }

            // 변수의기본값을 default 키워드로 설정
            // 변수를 선언 및 초기화 할 때, 해당 변수의 데이터 형식으로 초기화 한다.
            // 초기화 할 때 default 키워드로 초기화 가능

            int xxx = default;  // defalut 로 임시 할당, int 형의 기본값 0 할당
            bool bd = default;  // bool 형의 기본값 false 할당
            Console.WriteLine(xxx);
            Console.WriteLine(bd);


            // 연산자
            // + - * /
            // 대입 산술 관계 비교 논리 증감 비트 시프트
            // 1개의 항을 연산하는 단항 연산자
            // 2개의 항을 연산하는 이항 연산자
            // 3개의 항을 연산하는 삼항 연산자

            // 연산자와 피연산자

            int num1 = 1000;
            int number = num1 + 1233;


            // 단항 연산자 +
            int num2 = -8;
            num2 = +num2;   // +8 로 부호 변경


            // (int) 변환 연산자


            // 할당 연산자
            // = : 대입 할당
            // +=  -=  *=  /=  %=       a += 10  ==  a = a + 10


            // 증감연산자
            // ++
            // --
            int m = 10;
            Console.WriteLine(m++);
            Console.WriteLine(++m);
            Console.WriteLine(m);

            // 선 연산 후 대입(전위 증감 연산)  ++m
            // 선 대입 후 연산(후위 증감 연산)  m++






            // 관계 연산자(비교 연산자) : >   <   >=   <=   ==   !=
            // 논리 연산자 : and   or   not
            //               &&    ||    !
            // 양쪽이 true 일 때 true : and
            // 양쪽 중 하나가 true 일 때 true : or
            // 반대로 뒤집기 : not
            Console.WriteLine(true || false);


            var i = 3;
            var j = 5;
            var r = false;
            r = (i == 3) && (j != 3);   // true
            Console.WriteLine(r);
            r = (i != 3) || (j == 3);   // false
            Console.WriteLine(r);


            // 조건 연산자
            // 조건 연산자는 조건에 따라 true일 때와 false 일때 결과를 다르게 반환한다.
            // ? : 형태로 사용
            // 조건문 ? true 일 경우 실행 할 코드 : false 일 경우 실행 할 코드
            Console.WriteLine((5 > 3) ? "TRUE" : "FALSE");


            // sizeof()
            // sizeof(int)  //  4




            // if
            // if(조건식)
            // {
            //      실행문
            // }


            // python : if    elif    else
            // c# : if    else if    else
            int aaa = 100;
            if (aaa > 100)
            {
                Console.WriteLine(aaa);
            }
            else if (aaa == 100)
            {
                Console.WriteLine(aaa);
            }
            else 
            {
                Console.WriteLine(aaa); 
            }
            */

            /*
            // ex) 사용자에게 문자를 입력받아서 해당 문자에 대한 ascii 상 해당 문자에 대응하는 10진수 숫자가
            //     100보다 큰 문자라면 100보다 크라 라고 출력
            //     그렇지 않으면 입력 문자에 해당하는 숫자와 문자 출력
            Console.Write("문자 입력 : ");
            int input_char = Console.Read();        // char 입력받을 땐 Console.Read()

            if (input_char > 100)
            {
                Console.WriteLine("100보다 크다");
            }
            else
            {
                Console.WriteLine("{0}, {1}",input_char, Convert.ToChar(input_char));
            }
            */

            /*
            // switch 문
            // 조건문

            // switch(식)
            // {
            //      case 값1:
            //          실행문1;
            //          break;
            //      case 값2:
            //          실행문2;
            //          break;
            //      case 값3:
            //          실행문3;
            //          break;
            // }

           
            int user = Console.Read();
            switch (user)
            {
                case 65:    // A 입력
                    Console.WriteLine("A를 입력했다.");
                    break;
                case 66:
                    Console.WriteLine("B를 입력했다.");
                    break;
                case 67:
                    Console.WriteLine("C를 입력했다.");
                    break;

                default:
                    Console.WriteLine("해당 x");
                    break;
            }



            // for문
            // for(int i=0; i < 10; i++)        (선언문; 조건문; 증감문)
            // {
            //      실행문;
            // }
            // i 가 0부터 10보다 작을 때까지 매 바퀴 i가 1씩 증가하면서 실행문 반복
            for(int k = 0; k<10; k++)       // == for i in range(10)
            {
                Console.WriteLine(k);
            }


            // 무한루프
            // for(;;)
            */

            /*
            // 연습) 구구단 가로 출력
            for (int i = 2; i<10;i++)
            {
                Console.Write($"   {i}단\t");
            }
            for (int j = 1; j<10; j++)
            {   
                Console.WriteLine();
                for (int k = 2; k<10; k++)
                {
                    Console.Write($"{k}*{j}={k*j, 2}  ");
                    //if (k * j >= 10)
                    //{
                    //    Console.Write($"{k}*{j}={k * j}\t");
                    //}
                    //else
                    //{
                    //    Console.Write($"{k}*{j}= {k * j}\t");
                    //}
                }
            }
            Console.WriteLine();
            Console.WriteLine();
            */


            /*
            // while 문
            // while(조건식)
            // {
            //      실행문;
            // }
            int count = 0;
            while (count < 3)
            {
                Console.WriteLine("while 내부");
                count++;
            }



            // do-while 문
            // do
            // {
            //      실행문;
            // }while(조건식);
            count = 0;
            do
            {
                Console.WriteLine(count);
                count++;
            } while (count != 0);
            // do while 문은 첫 반복은 무조건 실행한다.
            // 조건식인 while이 뒤에 있기 때문에
            */

            // foreach
            // 배열이나 컬렉션 같은 요소를 여러 개 담은 데이터 구조에
            // 각 데이터가 들어있는 만큼 반복
            // 파이썬의 for문과 동일
            //foreach(항목 in 항목들)
            //{
            //    실행문;
            //}

            /*
            // 배열 선언시 요소들의 타임에 맞게 자료형을 작성해야한다.
            // ex) int[] numbers = {1, 2, 3, 4, 5};     // int 형 배열
            string[] names = { "C#", "python" };        // string[] i = {} : 문자열 배열
            foreach (string name in names)
            {
                Console.WriteLine(name);
            }


            // break, continue 는 파이썬과 동일


            // 배열이란
            // 동일한 데이터 형식을 갖는 데이터의 집합체
            // 배열을 사용해서 여러 데이터를 모아서 관리 가능


            // 컬렉션
            // collection
            // c# 에서 컬렉션은 배열, 리스트, 딕셔너리가 있다.

            // new 키워드는 캑체를 새로 생성할 때 쓰는 키워드
            // 배열
            var array = new string[] { "AAA", "BBB", "CCC" };
            foreach(string name in array)       // 요소로 문자열을 가져옴 -> string name in array
            {
                Console.WriteLine(name);
            }

            // 리스트
            var list = new List<string> { "L1", "L2", "L3" };
            foreach(string name in list)        // 요소로 문자열을 가져옴
            {
                Console.WriteLine(name);
            }

            // 딕셔너리
            var diction = new Dictionary<int, string> { { 0, "000" }, { 1, "111" }, { 2, "222" } };
            foreach(var name in diction)        // 요소로 정수형과 문자열을 가져옴 ->  var 능동적으로 할당하기
            {
                Console.WriteLine(name.Key);
                Console.WriteLine(name.Value);
            }



            // 배열
            // 순서가 있는 집합
            // 각 요소는 인덱스로 접근
            // 인덱스는 0부터
            // * 배열은 데이터 형식이 동일한 요소들을 포함
            // * 배열 new 키워드로 생성 가능
            // 배열에서 값 하나는 요소 element 혹은 항목 item 으로 표현
            // 반복문 foreach 와 조합하여 사용 가능
            // * 필요한 요소의 수를 미리 정해서 메모리를 적게 사용 사능


            string str1 = "c#9.0";
            Console.WriteLine(str1[0]);
            Console.WriteLine(str1[1]);
            Console.WriteLine(str1[2]);

            Console.WriteLine("ABC"[2]);

            // 배열은 데이터 형식 이름 뒤에 [] 기호를 사용하여 선언
            //타입[] 변수명;
            int[] numArr;
            // 배열 선언 후 new연산자(키워드)를 사용하여 배을의 크기만큼 메모리 영역을 잡을 수 있다.
            numArr = new int[3];    // 앞에 선언한 numArr 변수에 3칸 크기의 정수 배열을 선언

            int[] numArr1 = new int[5];
            // 데이터 형식[] 변수명 = new 데이터 타임[크기];

            // 1차원 배열
            int[] intnum = new int[10];
            // 배열의 요소 : 첨자 하나를 가지는 배열
            // 메모리 상 10개 공간이 잡힌다.
            // 0~9 까지 연속적으로 메모리 공간 잡힌다.
            intnum[0] = 100;


            int idx = 1;
            int[] xxxxx = { 1, 2, 3 };   // new 키워드 없이 배열 선언 및 초기화
            Console.WriteLine(xxxxx[idx]);
            Console.WriteLine(xxxxx[idx++]);
            */

            /*
            // 문제/*1) 5칸의 정수 배열을 new로 생성하고 각 요소에 1~100사이 임의 숫자 할당
            //       인덱스를 활용해서 배열에 저장되어 있는 값들의 합과 평균을 소수점 2번째 자리까지 출력
            int[] numArray = new int[5] { 23, 68, 13, 45, 97 };
            float sum = 0;
            foreach (int num in numArray)
            {
                sum += num;
            }
            Console.WriteLine($"합:{sum},  평균{sum / 5:0.00}");


            // 문제2) 5칸 짜리 1차원 정수 배열을 선언하고 사용자에게 5번동안 숫자를 입력 받아
            //        위 배열에 값을 할당한다
            //        배열에 저장된 값들의 총 합을 출력한다.

            int sum2 = 0;
            for (int i = 0; i < numArray.Length; i++)
            {

                //numArray[i] = int.Parse(Console.ReadLine());
                numArray[i] = (int) Console.Read();
                //numArray[i] = Console.Read();     // 값 입력 후 enter 를 치면 \n 까지 값으로 입력 됨 -> 뒤에 나오는 코드 스킵
                Console.ReadLine();
                Console.WriteLine(numArray[i]);
                sum2 += numArray[i];
            }
            Console.WriteLine(sum2);
            */

            /*
            char[] chararr = new char[5];
            for (int b=0; b<chararr.Length; b++) 
            {
                Console.WriteLine("입력하세요");
                int inputValue = Console.Read();
                Console.ReadLine();         // \n 문자 입력 처리용 코드
                chararr[b] = (char)inputValue;
            }
            Console.WriteLine("입력값");
            foreach(char c in chararr) 
            {
                Console.WriteLine(c);
                Console.WriteLine(c.GetType());
            }
            */



            /*
            // 다차원 배열
            // 차원이 여러개
            // 2차원 3차원 ~~~
            // 데이터 형식[ , ] 배열이름;        // 2차원 배열
            // 데이터 형식[ , , ] 배열이름;      // 3차원 배열
            // arr[0,0]

            int[] arr1;     // 1차원
            int[,] arr2;    // 2차원
            int[,,] arr3;   // 3차원

            arr1 = new int[2] { 1, 2 };
            arr2 = new int[2, 2] { { 1, 2 }, { 3, 4 } };
            arr3 = new int[2, 2, 2] { { { 1, 2 }, { 3, 4 } }, { { 5, 6 }, { 7, 8 } } };


            // 예제) 
            char[,] arrchar = new char[2, 2];
            arrchar[0, 0] = 'A';
            arrchar[0, 1] = 'B';
            arrchar[1, 0] = 'C';
            arrchar[1, 1] = 'D';

            Console.WriteLine($"{arrchar[0, 0]}");  // 표데이터 / 데이터 프레임 / 엑셀
            */


            /*        
            // 문제1) 2차원 배열 선언 및 초기화 문제
            // 2X3짜리 2차원 배열을 선언하고
            // 2차원 배열 내부에 임의의 값을 할당
            // 2차원 배열 내부에 배치된 요소 값을 전부 출력하는데
            // 행 열 구조의 표 처럼 보이도록 출력

            int[,] arrayInt = new int[2, 3] {
                { 1, 2, 3 },
                { 4, 5, 6 }
            };

            for (int i = 0; i < 2; i++)
            {
                for (int j = 0; j < 3; j++)
                {
                    Console.Write($"{arrayInt[i,j]}\t");
                }
                Console.WriteLine();
            }
            */
            /*
            // 문제2) string 3차원 배열 2x2x2 를 선언하고 3차원 배열의 모든 요소에 값을 할당
            // 3차원 3중 for 문 사용해서 요소 모두 출력

            string[,,] arrayStr = new string[2, 2, 2] 
            {
                { 
                    { "a1", "a2" },
                    { "a3", "a4" } 
                },
                { 
                    { "b1", "b2" },
                    { "b3", "b4" } 
                } 
            };

            for (int i = 0; i < 2; i++)
            {
                for(int j = 0; j < 2; j++)
                {   
                    //Console.WriteLine($"{i+1,4}층{j+1,4}행");
                    for(int k = 0; k < 2; k++)
                    {
                        Console.Write($"{arrayStr[i, j, k],6}");
                    }
                    Console.WriteLine();
                }
                    Console.WriteLine();
            }

            Console.WriteLine("-----------------------");

            string[,,] arrayStr2 = new string[2, 3, 4] {
                {
                    { "a1", "a2", "a3", "a4" },
                    { "a5", "a6", "a7", "a8" },
                    { "a9", "a10", "a11", "a12" }
                },
                {
                    { "b1", "b2", "b3", "b4" },
                    { "b5", "b6", "b7", "b8" },
                    { "b9", "b10", "b11", "b12" }
                }
            };

            for (int i = 0; i < arrayStr2.GetLength(0); i++)
            {
                for(int j = 0; j < arrayStr2.GetLength(1); j++)
                {   
                    //Console.WriteLine($"{i+1,4}층{j+1,4}행");
                    for(int k = 0; k < arrayStr2.GetLength(2); k++)
                    {
                        Console.Write($"{arrayStr2[i, j, k],6}");
                    }
                    Console.WriteLine();
                }
                    Console.WriteLine();
            }
            */


            /*
            // 가변 배열
            // 차원이 2개 이상인 배열은 다차원 배열
            // 배열 길이가 가변 길이인 배열은 가변배열
            // 데이터 형식[][] 배열이름; 형태로 사용
            // 다차원 배열은 데이터 형식[,] 배열이름;

            int[][] ints = new int[2][];    // [2][]형태로 두번째를 비워둠
            // 비워둔 자리에 동적으로 동적으로 n개 도기화 가능
            ints[0] = new int[] { 1, 2 };       // 0번째 행에 데이터 2개 저장
            ints[1] = new int[] { 3, 4, 5 };    // 1번째 행에 데이터 3개 저장

            // 위 배열의 요소를 이중 for 사용하여 콘솔에 출력
            for (int i=0; i < 2; i++) 
            {
                for (int j=0; j < ints[i].Length; j++)
                {
                    Console.WriteLine(ints[i][j]);
                }
                Console.WriteLine();
            }
            Console.WriteLine();
            */

            /*
            // 함수
            // 함수 function 혹은 메서드 method 는 재사용을 목적으로 만든
            // 특정 작업 수행 코드 블럭이다.
            // C#에서 진입점을 의미하는 함수는?  Main() 함수 -> 특수한 함수
            // 내장함수 or 사용자 정의 함수
            // 내장함수는 C#에서 자주 사용하는 기능을 미리 만들어 제공하는 함수
            // 내장함수는 특정 클래스의 함수로 표현된다.
            // 위 내장함수들을 API로 표현함
            // 사용자 정의 함수는 개발자가 만든 함수

            // 사용자 정의 함수의 기본 형태
            // static void 함수명()
            // {
            //      함수 실행문;
            // }

            // 함수 호출의 형태
            // 1. 함수이름();  : 단순 호출
            // 2. 함수이름(매개변수);  : 매개변수 포함한 호출
            // 3. 변수 = 함수이름(매개변수);  리턴(반환값)이 있는 호출

            myfunc();

            // 매개변수(인자)
            // 가변 매개변수 (여러개 인자)
            // C# 에서는 클래스 하나에 매개변수의 형식과 개수를 다르게 하여
            // 이름과 동일한 함수를 여러 개 만들 수 있다.
            // : 함수 오버로드    ex) myfunc() / myfunc(a) / myfunc(a,b)
            // 반환값(return)

            ShowMessage("hello");

            string returnValue = GetString();
            Console.WriteLine(returnValue);

            int result = intFunc(10);
            Console.WriteLine(result);


            // static void : 반환값 없음
            // static int : 정수형 반환
            // static string : 문자열 반환
            


            // 문제) 하나의 숫자를 매개변수를 통해 입력받아서
            // 해당 숫자가 음수 혹은 양수로 들어와도 절대값으로 리턴해주는 함수 생성
            // 함수의 이름은 myabs로 생성

            Console.WriteLine(myabs(-8));
            */


            /*
            // 매개변수 
            // 함수 내 선언되는 변수
            // 기본 매개변수 default
            // 선택적 매개변수 optional
            // 명명된 매개변수 named
            static void xxx(int x)
            {
                Console.WriteLine(x);
            }

            static void mysum(int first, int second)
            {
                Console.WriteLine(first + second);
            }

            mysum(100, 200);
            mysum(second: 100, first: 500);


            GetNum(1234);       // int 매개변수 GetNum 함수 호출
            GetNum(1234L);      // long 매개변수 GetNum 함수 호출


            // 함수의 범위
            // 클래스와 같은 레벨에 선언된 변수를 전역변수 혹은 필드라고 함
            // 함수 레벨에서 성너된 변수를 지역변수라고 함
            // 동일한 이름으로 변수를 전역변수와 함수 내의 지역변수로 선언 가능
            // 함수 내에서는 함수 범위에 있는 지역 변수를 사용한다.
            // 함수 범위 내에 선언된 변수가 없으면 전역변수 내에 선언된 변수를 사용한다.
            // C# 에서는 전역변수라는 표현 보다는 필드라느 표현을 주로 씀
            // 전역변수(필드)에는 언더스코어를 붙여 변수명을 작성하는 경우가 많음_result 형태



            // 화살표 함수 : =>
            // 화살표 모양의 연산자를 작성하여 메서드 코드를 줄일 수 있다.
            // 화살표 함수 arrow function
            // 람다식과 비슷한 개념
            static void Hi() => Console.WriteLine("hi");
            static void Multiplex(int a, int b) => Console.WriteLine(a * b);
            Hi();
            Multiplex(15, 8);
            // {}를 생략하고 => 로 작성
            */


            /*
            // 클래스, 구조체, 열거형, 네임스페이스
            // 닷넷에서 제공하는 대부분의 API는 클래스 형태
            // 클래스 : Console 클래스, String 클래스 등 대부분 클래스 구조임
            // 구조체 : DateTime 구조체, TimeSpan 구조체 형태로 표현, 클래스와 거의 동일하게 사용
            // 열거형 : Color 열거형 등, 특정 목록을 관리하기에 편리함
            // 네임스페이스 : System 네임스페이스처럼 여러 클래스, 구조체, 열거형을 포함한 단위
            // * API : Application Program Interface



            // Math 를래스
            // 닷넷에서 제공하는 수학 관련 내장 클래스 math
            // Math.PI          원주율
            // Math.Abs()       절대값
            // Math.Max()       최대값
            // Math.Min()       최소값
            // Math.Pow()       거듭제곱
            // Math.Floor()     지정된 10진수보다 작거나 같은 최대 정수값 반환
            // Math.Ceiling()   지정된 10진수보다 크거나 같은 정수값 반환
            // Math.Round()     특정 자리에서 반올림
            
            Console.WriteLine($"3.15를 소수점 둘째자리에서 반올림: {Math.Round(3.15, 1)}");
            // 3.14 를 소수점 첫번째 자리까지만 표현 == 소수점 두번째 자리에서 반올림 





            // 구조체 struct   ==  python : list
            // 하나의 이름으로 서로 다른 데이터 형식을 묶어 관리하는 구조체
            // 변수: 이름 하나, 공간 하나
            // 배열: 이름 하나, 데이터 형식 동일 공간 여러개 int[] xx = { 1, 2, 3 }
            // int, string 등 서로 다른 자료를 한 집단으로 정의 : 구조체
            // c# 에서는 구조체를 확장한 클래스 개념을 제공한다.
            // 클래스가 더 상위 개념이고 주로 사용하기에
            // 구조체는 이미 내장되어 있는 datetime 구조체 등을 불러서 사용할 때 많이 사용한다.
            // 따로 만드는 경우는 별로 없음. 대신에 클래스로 만듦



            // 구조체의 선언
            // struct 구조체이름
            // {
            //      데이터 형식 변수1;
            //      데이터 형식 변수2;
            // }

            Point xxxx;        // 구조체 생성
            xxxx.x = 100;      // point 구조체 내부 변수 x 에 100대입
            xxxx.y = 200;
            WriteLine(xxxx.x);  // 구조체 내부 변수 출력


            // 구조체 : int or string 등 데이터 타입을 만든 것
            // 구조체 배열
            // 구조체[] 배열이름 = new 구조체[100];   


            static void Print(string name, int age) => WriteLine($"name: {name}  age: {age}");

            Profile profile;
            profile.Name = "홍길동";
            profile.Age = 20;
            Print(profile.Name, profile.Age);

            Profile[] names = new Profile[2];
            names[0].Name = "1번 이름";
            names[0].Age = 100;
            names[1].Name = "2번 이름";
            names[1].Age = 200;

            for (int i=0; i<names.Length; i++)
            {
                Print(names[i].Name, names[i].Age);
            }
            */

            /*
            // 학생이라는 구조체를 만들고
            // 학생 구조체는 학생의 이름/국어/영어/수학 점수가 있다.
            // 학생은 총 10명, 10명의 정보를 하나의 students 라는 배열에 배치한다.
            // 모든 학생의 점수 정보는 임의로 코드상 기재한다.

            // printAvg 라는 함수를 선언하고
            // printAvg 함수는 학생 10명의 정보를 담은 하나의 배열을 전달 받는다.
            // printAvg 함수의 반환값 : 문자열 형태이고 평균점수가 가장 높은 학생의 이름을 return


            Random rand = new Random();
            Student[] students = new Student[5];
            for (int i =0; i<students.Length; i++)
            {
                students[i].name = $"{i+1}번학생";
                students[i].kor = rand.Next(0, 101);
                students[i].eng = rand.Next(0, 101);
                students[i].math = rand.Next(0, 101);
            }

            static string printAvg(Student[] array)     // 배열 매개변수 : static string 함수명( 참조배열이름[] 매개변수)   [] 대괄호 넣어야함
            {
                float avg = 0;
                string person = "";
                for (int i = 0; i < array.Length; i++)
                {
                    int sum = array[i].kor + array[i].eng + array[i].math;
                    Console.WriteLine($"이름:{array[i].name,5}    합:{sum,4}   평균:{sum / 3F,6:0.00}");
                    if (avg <= sum / 3)
                    {
                        avg = sum / 3F;
                        person = array[i].name;
                    }
                }
                return $"{person}, {avg:0.00}";
            }

            Console.WriteLine(printAvg(students));
            */


            /*
            // 내장형 구조체
            // DateTime : 시간/날짜 간격에 대한 정보를 제공
            // Timespan : 시간/날짜 계산 정보 제공
            // Char : 문자 관련 정보 제공

            WriteLine(DateTime.Now);
            WriteLine(DateTime.Now.ToString());
            WriteLine(DateTime.Now.Year.ToString());
            WriteLine(DateTime.Now.Hour.ToString());
            WriteLine(DateTime.Now.Minute.ToString());


            // ms 까지 표현 가능

            TimeSpan Dday = Convert.ToDateTime("2025-12-12") - DateTime.Now;
            WriteLine(Dday.ToString());

            // 조건식이 참이라면 out 뒤에 나오는 변수를 반환한다.
            if (DateTime.TryParse("2024/12/12", out DateTime d))        // 인라인 out 변수 : 변수가 선언되고 바로 사용할 수 있게 됨
            {
                Console.WriteLine(d.ToString());
            }




            // DateTime 구조체의 AddHours() 메서드
            // 보통의 1년 : 365일 : 8760시간
            // 1년을 시간 단위로 8760단계로 표현 가능


            static DateTime myGetTime(int num)
            {
                return new DateTime(2024,1,20,0,0,0).AddHours(--num);
            }
            Console.WriteLine(myGetTime(1));
            Console.WriteLine(myGetTime(8760));
            */


            // 열거형 enum
            // 타입 이름 하나로 서로 관련 있는 항목들을 묶어 관리하는 열거형 타입
            // 열거형 타입은 기억하기 어려운 상수들을 이름을 지어 관리/표현하는 방식
            // 열거형을 사용하면 값 리스트 여러개를 이름 하나로 관리할 수 있다.
            // 열거형은 enum 키워드를 사용

            // ConsoleColor 열거형

            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("Blue");
            Console.BackgroundColor = ConsoleColor.Yellow;
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Red");
            Console.ResetColor();


            Level x = Level.High;
            Console.WriteLine(x);


            Console.WriteLine(Align.Left);              // Left
            Console.WriteLine((int) Align.Left);        // 4

            Console.WriteLine((int)Align.Bottom);       //  1       // 전 값 + 1 출력 (비어있으면 0+1)

            Console.WriteLine("-------------------------");
            Type cc = typeof(ConsoleColor);
            Console.WriteLine(cc);
            string[] colors = Enum.GetNames(cc);    // GetNames : 지정된 열거형에서 상수 이름 배열 리턴
            foreach (string color in colors)
            {
                Console.WriteLine(color);
            }









        }
    }
}