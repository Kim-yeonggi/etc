//using System;   // 네임스페이스에 대한 선언부
using static System.Console;
using static System.Math;

namespace Helloworld    // 네임스페이스 지정
{
    class Program   // 클래스명 지정
    {
        static void Main()  // 함수 선언
        {
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











        }   
    }
}