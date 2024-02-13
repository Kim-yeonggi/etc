using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//namespace ConsoleApp3
//{
//    internal class Program
//    {
//        public static string GetName()
//        {
//            return "이름";
//        }

//        static void Run()
//        {
//            Console.WriteLine("ClassNote 클래스의 Run메서드 호출");
//        }
//        static void Main(string[] args)
//        {
//            // C#의 모든 모드에 반드시 들어가는 클래스 구조
//            // 닷넷의 공용 형식 시스템의 기본 구문
//            // 클래스는 데이터와 함수를 묶은 구조
//            // 클래스 속성(데이터), 메서드(로직)
//            // 내장 클래스와 사용자 정의 클래스
//            // Console, String, Math 등 내장 클래스
//            // 클래스는 객체(개체)를 생성하는 템플릿

//            // public class 클래스 이름{
//            // 클래스 내부 코드
//            // 클래스 내부 코드
//            // 클래스 내부 코드
//            // }

//            // public 키워드는 생략 가능하지만 여러 클래스를 사용할 때는 public을 써야 한다.
//            // public : 공용
//            // private : 공개 X

//            Run();  // 메서드() : 메서드 레벨 호출 : 같은 클래스의 메서드 호출 1
//            Program.Run();  // 클래스명.메서드() : 클래스 레벨의 호출 : 특정 클래스의 메서드 호출 2
//            // 1번 방식이 가능한 이유는 현재 Run 메서드가 Main 메서드와 같은 클래스에 있기 때문에
//            // 호출하려는 메서드가 다른 클래스에 있따면 2번 방식 사용 해야함.

//            // static과 정적메서드
//            // C#에서는 static 을 정적으로 표현
//            // 정적 선언된 것은 공유될 수 있다를 의미
//            // 스태틱이 붙는 클래스의 모든 멤버는 해당 클래스 내에서 누구나 공유해서 접근 가능
//            // 메서드에 스태택이 붙는 메서드를 정적 메서드라고 하는데, 공유 메서드라고도 표현

//            Console.WriteLine(GetName());

//            // C# 기본 프로그래밍 단위는 클래스로 샛체를 생성해서 
//        }
//    }
//    public class myclass
//    {
//        static void Run()
//        {
//            Console.WriteLine();
//        }
//    }
//}

/*
class MyFirstClass
{
    static void StaticMethod() => Console.WriteLine("정적 메서드");
    // 클래스 공용
    void instanceMethod() => Console.WriteLine("인스턴스 메서드");
    // 객체가 호출하는 메서드

    void Sum(int num1, int num2)
    {
        Console.WriteLine(num1 + num2);
    }
    void Sub(int num1, int num2)
    {
        Console.WriteLine(num1 - num2);
    }
    void Div(int num1, int num2) => Console.WriteLine(num1 / num2);
    void Mul(int num1, int num2) => Console.WriteLine(num1 * num2);

    static void Main()
    {
        //MyFirstClass.StaticMethod();
        //MyFirstClass.instanceMethod();    // 인스턴스를 통해 접근 가능

        MyFirstClass myFirstClass = new MyFirstClass(); // 인스턴스 선언 및 할당
        //myFirstClass.instanceMethod();


        // 숫자 두 개를 입력 받아 연산하는 더하기 빼기 나누기 곱하기 함수를 만들고
        // 인스턴스를 통해서만 사용가능하도록 구성
        // main 안에서는 자유롭게 사칙연산 함수 호출
        string n1 = Console.ReadLine();
        string n2 = Console.ReadLine();
        //num1 = Convert.ToInt32(num1);
        int num1 = int.Parse(n1);
        int num2 = int.Parse(n2);
        
        myFirstClass.Sum(num1, num2);
        myFirstClass.Sub(num1, num2);
        myFirstClass.Div(num1, num2);
        myFirstClass.Mul(num1, num2);

        // static 붙은 정적 메서드는 클래스명 메서드() 로 호출 : 정적 멤버, 공유 멤버
        // static 붙지 않은 메서드는 인스턴스.메서드()로 호출 : 인스턴스 멤버
    }
}
*/

/*
public class MyClass
{
    public static void MyMethod()
    {
        Console.WriteLine("클래스 메서드");
    }
    // 현재 이 클래스 내부에는 public 키워드가 붙어있음
    // 이 클래스 내부 MyMethod 도 public이 붙어있음
    // 클래스를 public으로 설정했기에 외부에서 접근 가능(public = 공용)
    // public 을 액세스(접근) 한정자라고 함
    // 대부분 클래스와 메서드를 public을 작성하는 것을 기본으로 함
    // public 을 작성하지 않으면 internal로 작동
}

class ClassDescription
{
    static void Main()
    {
        MyClass.MyMethod();
    }
}
*/

/*
public class ClassName
{
    public static void Membername()
    {
        Console.WriteLine("클래스의 멤버가 호출");
    }
}
*/

/*
public class ClassAndMember
{

    //public static void Main()
    //{
    //    ClassName.Membername();
    //    Console.WriteLine(Environment.Version);
    //    Console.WriteLine(Environment.OSVersion);
    //    Console.WriteLine(Environment.UserName);
    //    Console.WriteLine(Environment.CurrentDirectory);
    //    Console.WriteLine(Environment.MachineName);
    //    // Environment.Exit(0);    // 닷넷 프레임워크에 내장된 클래스로 Exit 메서드를 통해 프로그램 강제 종료
    //    // 시스템 환경 변수
    //    Console.WriteLine("-----------------------------------------------------------");

    //    //Process.Start("Notepad.exe");   // 프로세스 관련 클래스
    //    //Process.Start("Chrome.exe", "https://naver.com");
    //    // // exe 파일 실행 Start 함수

    //    // Random
    //    // 난수 생성
    //    Random random = new Random();
    //    Console.WriteLine(random.Next());   // 임의의 정수 출력
    //    Console.WriteLine(random.Next(5));   // 0~4 호출
    //    Console.WriteLine(random.Next(1, 10));  // 1~9 임의 수
    //    Console.WriteLine(random.NextDouble()); // 임의의ㄹ 실수 반환
    //}
    public static void Main()
    {
        // 특정 중복없는 당첨번호를 지정해놓고 랜덤으로 뽑은 숫자 6개와 동일한지 검사하는 코드 작성
        // Random 클래스 활용
        // Random으로 뽑은 숫자는 배열에 담아서 관리함.
        int[] numbers;
        numbers = new int[6];
        Random random = new Random();
        int[] result = new int[6] { 1, 2, 3, 4, 5, 6 };
        int count = 0;
        for(int i=0; i<numbers.Length; i++)
        {
            int temp_num = random.Next(1, 45);
            if (Array.IndexOf(numbers, temp_num) == -1)
            {
                numbers[i] = temp_num;
                if (Array.IndexOf(result, numbers[i]) != -1)
                {
                    count++;
                }
            }
            else
            {
                --i;
            }
        }

        if (count == 6)
        {
            Console.WriteLine(true);
            Console.WriteLine(count);
        }
        else 
        { 
            Console.WriteLine(false);
        }
    }
}

// 액세스 한정자 public 외 다른 종류
// private
// internal(디폴트)
// sealed



// String : 가장 많이 사용하는 문자열 처리 관련 속성 메서드 제공 클래스
// StringBuilder : 대용량 문자열 처리 관련 속성 및 메서드
// Array : 배열 관련 주요 메서드 및 속성
*/

namespace Consolecp3
{
    public class CheckMember
    {
        public static void Main()
        {
            // 합계
            // 개수
            // 평균

            // 최대 최소
            /*
            int[] numbers = { -2, -5, -3, -7, -1 };     // 최대값, 최소값 알고리즘 구현
            int maxNum = 0;
            int minNum = 0;
            for(int i=0; i<numbers.Length-1; i++)
            {
                if (numbers[i] > numbers[i+1])
                {
                    maxNum = numbers[i];
                }
                else
                {
                    maxNum = numbers[i+1];
                }
                
                if (numbers[i] < numbers[i+1])
                {
                    minNum = numbers[i];
                }
                else
                {
                    minNum = numbers[i+1];
                }
            }
            Console.WriteLine($"최대값 : {maxNum} \n최소값 : {minNum}");

            Console.WriteLine("---------------------------------------------");
            Array.Sort(numbers);
            minNum = numbers[0];
            maxNum = numbers[numbers.Length-1];
            Console.WriteLine($"최대값 : {maxNum} \n최소값 : {minNum}");
            */


            // 순위
            /*
            int[] scores = { 90, 87, 100, 95, 80 };
            int[] ranking = Enumerable.Repeat(1, 5).ToArray();

            for (int s = 0; s < scores.Length; s++)
            {
                for (int i = 0; i<scores.Length; i++)
                {
                    if (scores[s] <= scores[i])
                    {
                        ranking[s]++;
                    }
                }
                Console.WriteLine($"{scores[s]} : {ranking[s]-1}");
            }
            */


            // 정렬 오름차순 내림차순
            /*
            // 선택 정렬 : 데이터 하나 기준으로 나머지 데이터와 비교하여 자리를 바꾸는 행위를 반복, Temp 임시 변수 사용
            int[] numbers = { 5, 3, 4, 1, 2 };
            int Temp = 0;

            for (int i = 0; i < numbers.Length; i++)
            {
                for (int j = i+1; j < numbers.Length; j++)
                {
                    if (numbers[i] > numbers[j])
                    {
                        Temp = numbers[i];
                        numbers[i] = numbers[j];
                        numbers[j] = Temp;
                    }
                }
            }

            foreach (int i in numbers) { Console.WriteLine(i); }
            */


            // 검색 : 이진 검색 : 정렬이 되어있다는 가정하에 가능
            /*
            int[] data = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };
            int n = data.Length;
            int search = 1;
            bool flag = false;
            int index = -1;
            int count = 0;

            int low = 0;
            int high = n-1;
            while (low <= high)
            {
                count++;
                int mid = (low + high) / 2;
                if (data[mid] == search)
                {
                    flag = true;
                    index = mid;
                    break;
                }
                if (data[mid] > search)
                {
                    high = mid - 1;
                }
                else
                {
                    low = mid + 1;
                }
            }
            if (flag)
            {
                Console.WriteLine($"숫자 {search}, 위치 {index}, 시도횟수 {count}");
            }
            else
            {
                Console.WriteLine("none");
            }
            */

            // 병합

            // 최빈값
        }
    }
}
