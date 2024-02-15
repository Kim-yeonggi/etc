// using Korea.Seoul;
using ConsoleApp3;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

// using In = Korea.Incheon;


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


//namespace Consolecp3
//{
//    /*
//    namespace Y     // 중첩되어 있는 네임스페이스 내부 코드
//    {
//        public class XY
//        {
//            public void XYX() => Console.WriteLine("XYX");
//        }
//    }
//    namespace X
//    {
//        public class XY
//        {
//            public void XYX() => Console.WriteLine("XYX");
//        }
//    }

//    // System, System.Text 등 using으로 불러온 것들이 네임스페이스임
//    // 네임스페이스를 만드는 이유는 프로그램 큐모가 커질 때 클래스 이름 중복 등 충돌 방지 목적
//    // 네임스페이스를 다르게 만들면 동일한 클래스를 하나의 프로젝트에서 사용할 수 있다.
//    // 서로 관련있는 기능 클래스, 구조체, 열거형 등을 묶는 개념
//    // 클래스 이름 중복 방지
//    // 클래스 계층형 구조 형성
//    // 네임스페이스는 모듈의 의미와 비슷

//    // namespace 네임스페이스명 으로 네임스페이스 구간 작성
//    // 클래스와 마친가지로 첫 글자는 대문자로 작성(클래스와 동일)
//    */



//    //public class CheckMember
//    //{
//    //    // 240213
//    //    public static void Main()
//    //    {
//    //        // 합계
//    //        // 개수
//    //        // 평균

//    //        // 최대 최소
//    //        /*
//    //        int[] numbers = { -2, -5, -3, -7, -1 };     // 최대값, 최소값 알고리즘 구현
//    //        int maxNum = 0;
//    //        int minNum = 0;
//    //        for(int i=0; i<numbers.Length-1; i++)
//    //        {
//    //            if (numbers[i] > numbers[i+1])
//    //            {
//    //                maxNum = numbers[i];
//    //            }
//    //            else
//    //            {
//    //                maxNum = numbers[i+1];
//    //            }

//    //            if (numbers[i] < numbers[i+1])
//    //            {
//    //                minNum = numbers[i];
//    //            }
//    //            else
//    //            {
//    //                minNum = numbers[i+1];
//    //            }
//    //        }
//    //        Console.WriteLine($"최대값 : {maxNum} \n최소값 : {minNum}");

//    //        Console.WriteLine("---------------------------------------------");
//    //        Array.Sort(numbers);
//    //        minNum = numbers[0];
//    //        maxNum = numbers[numbers.Length-1];
//    //        Console.WriteLine($"최대값 : {maxNum} \n최소값 : {minNum}");
//    //        */


//    //        // 순위
//    //        /*
//    //        int[] scores = { 90, 87, 100, 95, 80 };
//    //        int[] ranking = Enumerable.Repeat(1, 5).ToArray();

//    //        for (int s = 0; s < scores.Length; s++)
//    //        {
//    //            for (int i = 0; i<scores.Length; i++)
//    //            {
//    //                if (scores[s] <= scores[i])
//    //                {
//    //                    ranking[s]++;
//    //                }
//    //            }
//    //            Console.WriteLine($"{scores[s]} : {ranking[s]-1}");
//    //        }
//    //        */


//    //        // 정렬 오름차순 내림차순
//    //        /*
//    //        // 선택 정렬 : 데이터 하나 기준으로 나머지 데이터와 비교하여 자리를 바꾸는 행위를 반복, Temp 임시 변수 사용
//    //        int[] numbers = { 5, 3, 4, 1, 2 };
//    //        int Temp = 0;

//    //        for (int i = 0; i < numbers.Length; i++)
//    //        {
//    //            for (int j = i+1; j < numbers.Length; j++)
//    //            {
//    //                if (numbers[i] > numbers[j])
//    //                {
//    //                    Temp = numbers[i];
//    //                    numbers[i] = numbers[j];
//    //                    numbers[j] = Temp;
//    //                }
//    //            }
//    //        }

//    //        foreach (int i in numbers) { Console.WriteLine(i); }
//    //        */


//    //        // 검색 : 이진 검색 : 정렬이 되어있다는 가정하에 가능
//    //        /*
//    //        int[] data = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };
//    //        int n = data.Length;
//    //        int search = 1;
//    //        bool flag = false;
//    //        int index = -1;
//    //        int count = 0;

//    //        int low = 0;
//    //        int high = n-1;
//    //        while (low <= high)
//    //        {
//    //            count++;
//    //            int mid = (low + high) / 2;
//    //            if (data[mid] == search)
//    //            {
//    //                flag = true;
//    //                index = mid;
//    //                break;
//    //            }
//    //            if (data[mid] > search)
//    //            {
//    //                high = mid - 1;
//    //            }
//    //            else
//    //            {
//    //                low = mid + 1;
//    //            }
//    //        }
//    //        if (flag)
//    //        {
//    //            Console.WriteLine($"숫자 {search}, 위치 {index}, 시도횟수 {count}");
//    //        }
//    //        else
//    //        {
//    //            Console.WriteLine("none");
//    //        }
//    //        */

//    //        // 병합

//    //        // 최빈값


//    //    }
//    //}



//    /*
//    // C#에서의 사용자 정의 클래스를 통한 인스턴스 생성시 new 키워드 사용
//    public class Counter
//    {
//        public void GetCount()  // GetCount는 static이 지정되지 않은 인스턴스 멤버 형태임
//                                // 인스턴스 멤버는 인스턴스를 통해 접근해야함
//        {
//            Console.WriteLine("count 100");
//        }
//    }
//    class ObjectNote
//    {
//        static void Main()
//        {
//            Counter counter = new Counter();    // 인스턴스 생성
//            counter.GetCount();     // 인스턴스를 통해 함수 호출
//        }
//    }
//    */



//    /*
//    public class MyMath
//    {
//        public void sum(int x, int y)
//        {

//            int sum = x + y;
//            Console.WriteLine(x + y);
//        }
//    }

//    class pro
//    {
//        void Main()
//        {
//            var mymath = new MyMath;    // var 키워드로 식별자 선언하는 방식 : 익명 방식 or 무명 방식

//            mymath.sum(3, 2);   
//            int[] x = new int[3];
//            // 정적 메버와 인스턴스 멤버
//            // 클래스 내에 선언되는 모든 멤버는 위 2가지 유형 중 하나이다.
//            // 정적 멤버이거나 인스턴스 멤버이거나
//            // 선언시 static 키워드를 붙이면 정적 멤버
//            // static 이 없으면 인스턴스 멤버
//            // static 키워드가 붙은 멤버에 접근시   클래스 이름.엠버 이름
//            // 인스턴스 멤버 접근 시   인스턴스명.멤버이름

//            // static이 붙은 변수는 클래스 변수라고 함
//            // static이 붙지 않은 변수는 인스턴스 변수라고 함
//            // static은 공유의 의미
//        }
//    }
//    */



//    /*
//    public class Category
//    {
//        public void Print(int i) => Console.WriteLine(i);
//    }
//    class ClassArray
//    {
//        static void Main()
//        {
//            Category[] category = new Category[3];  // 카테고리라는 클래스로 구성된 배열
//            category[0] = new Category();       // 카테고리라는 클래스도 데이터 타입 중 하나로 취급
//            category[1] = new Category();       // 해당 배열에는 카테고리 클래스의 인스턴스를 넣을 수 있따.
//            category[2] = new Category();

//            for (int i = 0; i < category.Length; i++)
//            {
//                category[i].Print(i);
//                Console.WriteLine(category[i].ToString());
//            }
//        }
//    }
//    */
//}


//namespace A
//{
//    public class Car
//    {
//        public void Go() => Console.WriteLine("A 네임스페이스의 Car Go");
//    }
//}

//namespace B
//{
//    public class Car
//    {
//        public void Go() => Console.WriteLine("B 네임스페이스의 Car의 Go");
//    }
//}

//namespace Namespace
//{
//    static void Main()
//    {
//        A.Car acar = new A.Car();   // 네임스페이스 A 에 있는 class Car를 통해 만든 인스턴스
//        B.Car bcar = new B.Car();   // 네임스페이스  B 에 있는 clas Car를 통해 만든 인스턴스
//        acar.Go();
//        bcar.Go();  // 네임스페이스가 적용되어 있는 클래스를 사용할 때 : 네임스페이스명.클래스 형태로 사용
//    }
//}


/*
namespace Korea
{
    namespace Seoul
    {
        public class Car
        {
            public void Run() => Console.WriteLine("서울 car run");
        }
    }

    namespace Incheon
    {
        public class Car
        {
            public void Run() => Console.WriteLine("인천 car run");
        }
    }
}

namespace NamespaceDescription
{
    class NamespaceDescription
    {
        static void Main() 
        {
            Korea.Seoul.Car s = new Korea.Seoul.Car();
            s.Run();
            Korea.Incheon.Car i = new Korea.Incheon.Car();
            i.Run();

            Car seoul = new Car();  // using Korea.Seoul
            seoul.Run();

            In.Car ic = new In.Car();   // using In = Korea.Incheon
            ic.Run();
        }
    }
}
*/

// 필드 : 클래스의 부품 역할, 클래스의 내부 상태 값 저장 용도의 변수 등
// 클래스 내에 선언된 변수 또는 배열 등을 c#에서 필드라고 표현한다.
// 필드는 대부분 private 액세스 한정자를 사용한다.
// 클래스 내에서 데이터를 담는 역할
// 필드는 개체의 상태를 저장한다.

// 필드는 선언 후 초기화하지 않아도 자동으로 초기화된다.
// int형 같은 경우는 0으로 초기화, string은 String.Empty(공백)로 자동 초기화
// bool 형은 false, obj 필드는 null 값으로 초기화



// 지역변수와 전역변수
// C#에서 변수 선언시 Main() 메서드 같은 메서드 내에서 선언하거나 메서드 밖에서 선언이 가능하다.
// 메서드 내에서 선언된 변수 또는 배열 등을 지역 변수라고 함.
// 메서드 밖에서 선언된 변수 또는 배열 : 전역 변수라고 함
// C#에서는 전역 변수라는 용어 사용하지 않고 메서드와 동일하게 엑세스 한정자를 붙여 필드라고 함


// 지역변수 : 메서드가 종료되면 변수는 자동 소멸
// 전역변수 (필드) : 메서드 내부가 아닌 클래스 내에 선언된 변수
// C#에서 필드는 변수와 마찬가지로 주로 소문자로 식별자 이름 시작

// 필드의 종류
// 변수 형식의 필드 : 지역 변수와 마찬가지로 값을 대입하여 사용 가능
// 상수 형식의 필드 : 필드와 비슷하지만 값을 한 번 초기화하면 다시 값을 바꿀 수 없음
// 읽기 전용 필드 : readonly 키워드를 붙이는 읽기 전용 필드도 상수 필드와 비슷한 역할, 상수와 차이점 : 초기화시키지 않아도 됨
// 배열 형식의 필드 : 배열을 필드레벨로 올린 개념, 값을 여러개 저장 가능
// 개체 필드 : object 와 여러 개체를 담는 필드

// public static int intNum : 정적인 정수 필드
// public string str : 인스턴스 형식의 문자 필드
// public int num : 인스턴스 정수 필드



// private : 외부에서 진입 X 감춤
// public : 외부에 공개
// protectied : 상속받은 대상만 접근 가능
// * 세가지 모두 현재 클래스 내부에서는 사용 가능 



/*
class Scope
{
    static string globalV = "전역변수";  // 전역변수 혹은 필드라고 표현
    static void Main()
    {
        string loclaV = "지역변수";
        Console.WriteLine(loclaV);  // 지역변수 출력
        Console.WriteLine(globalV); // 전역변수 출력
        Test();     // 같은 클래스(Scope) 내부에서 사용 -> 클래스명 없이 사용 가능 ( Scope.Test()) X )
    }
    static void Test() => Console.WriteLine(globalV);       // 전역변수 출력 함수
}
*/


/*
class Say
{
    private string message = "안녕하세요";
    public string message2 = "hello";
    public void Hi(string a)
    {
        //string message = "123";
        Console.WriteLine(message);
        this.message = a;    // this 키워드로 자신 클래스(say) 인스턴스인 개체 내부에 선언된 massage필드로 접근
        Console.WriteLine(message);
        
    }
}

class FieldInitializer
{
    static void Main()
    {
        Say say = new Say();
        say.Hi("반갑습니다.");
        Console.WriteLine(say.message2);
        say.message2 = "hello2222222";
        Console.WriteLine(say.message2);
    }
}
*/


/*
class Schedule
{
    private string[] weekDay = { "월", "화", "수", "목", "금", "토", "일" };
    public void PrintWeekDay()
    {
        foreach (string day in weekDay)
        {
            Console.WriteLine(day);
        }
        Console.WriteLine();
    }

    public static void XX()        // public 이 없으면 static 있어도 접근 불가
    {
        // 클래스로 접근 가능
        Console.WriteLine("XXXXXXXX");
    }

    public void XXX()       // 인스턴스로 접근 가능
    {
        Console.WriteLine("XXX#33333333333333");
    }
}

class FieldArray
{
    static void Main()
    {
        Schedule schedule = new Schedule();
        schedule.PrintWeekDay();
        schedule.XXX();     // public -> 인스턴스 접근
        Schedule.XX();      // public static -> 클래스 접근
    }
}
*/


/*
// C# 생성자 함수
// C#에서 생성자는 클래스에서 맨 먼저 호출되는 메서드로, 클래스 기본값 등을 설정한다.
// 개체를 생성하면서 하고자하는 코드를 작성하는 부분(초기화 작업)
// 생성자는 생성자 메서드라고도 함
// 생성자 함수의 이름은 클래스의 이름과 동일하게 작성한다.
// 생성자는 여러개가 선언될 수 있음
// 생성자를 여러개 만드는 경우 : 생성자마다 매겨변수를 다르게 설정하여 여러개 만들 수 있음.
// 메서드가 오버로드 되는것 처럼 생성자도 오버로드 됨
// 생성자 함수는 void를 포함한 반환값을 가지지 않는다.
// public 생성자 함수명  으로 작성


//class Car
//{
//    public Car()
//    {
//        Console.WriteLine("생성자 함수 호출");
//    }
//    static void Main()
//    {
//        var car = new Car();    // 인스턴스가 생성될 때 자동으로 생성자 호출 실행
//        Console.WriteLine("11111111111");
//    }
//}

//public class Dog
//{
//    private string name;
//    public Dog(string name)     // 매개변수 있는 생성자
//    {
//        this.name = name;
//    }
//    public string Cry()
//    {
//        return name + "Cry";
//    }
//}

//class pro
//{
//    static void Main()
//    {
//        Dog dog1 = new Dog("1번 강아지");       // 인스턴스 생성시 매개변수 전달해야 함.
//        dog1.Cry();

//        Dog dog2 = new Dog("2번 강아지");
//        dog2.Cry();
//    }
//}
*/

/*
namespace ConstructorParameter
{
    class My
    {

        // private : 인스턴스 필드
        private string _name;
        private int _age;
        private string _description = "ddddddd    ";

        
        public static string _x = "X";      // static : 공용 필드 (클래스 필드)

        public string pname { 
            get
            {
                //return "프로퍼티를 통한 이름 get";
                return _name;       // 항상 return 이 있어야함
            }
            set
            {
                _name = "프로퍼티를 통한 이름 set";
            } 
        }       // 프로퍼티 // "public 반환형식 프로피티명 {get; set;}" 으로 작성
        // 위 pname 프로퍼티는 get을 통해 프로퍼티값을 조회할 수 있고
        // set을 통해 프로퍼티값을 할당할 수 있음.
        // 프로퍼티도 static이 없기 때문에 이스턴스 마다 분리
        // 외부에 공개되는 필드라고 여김
        // set을 세터 get을 게터로 표현해도 됨

        //public string pname { get; set; }   // 초깃값

        //public string pname { get; private set; }   // set 에 private : 값 설정이 안됨 => 읽기 전용

        public My(string name, int age)
        {
            this._name = name;
            this._age = age;
            this._description += name;
            _x = name;      // 매개변수 있는  My가 호출되어야 _x 에 name 초기화
        }
        public My()
        {
            Console.WriteLine("생성자 호출");
        }

        public void PrintMy()
        {
            Console.WriteLine("{0} {1}",this._name, this._age);
        }

        public void PrintMy2()
        {
            Console.WriteLine(this._description);
            Console.WriteLine(_x);
        }
    }

    class ConstructorParameter
    {
        static void Main()
        {
            My myinfo = new My("name 전달", 222);
            myinfo.PrintMy();
            myinfo.PrintMy2();

            My my = new My();
            //my.PrintMy();

            my.PrintMy2();


            my.pname = "프로퍼티";                  // set
            Console.WriteLine(my.pname);        // get
            
            myinfo.pname = "프로퍼티2";              // set
            Console.WriteLine(myinfo.pname);    // get
            Console.WriteLine(my.pname);
        }
    }
}
*/


/*
// 문제) 클래스 필드, 인스턴트 필드, 프로퍼티의 get, 프로퍼티의 set, 메서드, 생산자를 포함하는 클래스 구조 만들기
// 계좌 클래스 만들기

// 입금
// 출금
// 송금(상대방 은행과 계좌번호를 입력해서 송금) : 인스턴스 간의 교류
// 잔액 조회 : 프로퍼티

// 생성자 함수에 추가
// 계좌번호 : 필드 private       ->  10자리 숫자, 앞 4자리 1111 고정, 다음 2자리 랜덤, 0001 부터 순차 증가
// 예금주 : 필드 private         ->  이름
// 은행명 : 필드 private         ->  myBank
// 통장 개설일 : 필드 private     date 클래스 활용해서 인스턴스 생성 시점으로 자동 배치 [연/월/일] 
// 


namespace CustomBank
{
    class Account
    {
        public static string bank = "mybank";

        private string myBank;
        private string myName;

        //public Random random = new Random();
        
        private string numberF = "1111";
        private string numberM;
        public static int numberL= 1;

        private string numbers;
        private string myDate;

        static Random rand = new Random();
        int num1 = rand.Next(0, 10);
        int num2 = rand.Next(0, 10);

        private int money;
        private string myMoney;
        public static string[] account_list;

        public static string[] member_list;
        
        public Account()
        {
            Console.Write("이름 입력: ");
            string name = Console.ReadLine();
            this.myName = name;
            this.myBank = bank;
            this.numberM = $"{num1}{num2}";
            this.numbers = this.numberF + numberM + numberL.ToString().PadLeft(4, '0');

            DateTime today = DateTime.Today;
            this.myDate = $"{today.Year}{today.Month}{today.Day}";
            this.money = 0;
            this.myMoney = money.ToString();

            account_list = new string[] { myBank, myDate, myName, numbers, myMoney };
            //Account.member_list[numberL - 1] = account_list;
            numberL++;
        }

        public void PrintMy()
        {
            Console.WriteLine($"{this.myBank}   이름 {this.myName}   계좌 {this.numbers}   개설일 {this.myDate}   잔액 {this.money}원");
        }

        public void Deposit()
        {
            Console.WriteLine($"입금 계좌 정보: 이름 {this.myName}   계좌 {this.numbers}   잔액 {this.money}원");
            Console.Write("입금할 금액 입력: ");
            string tempMoney = Console.ReadLine();
            int addMoney = Convert.ToInt32(tempMoney);
            this.money += addMoney;
            Console.WriteLine($"이름 {this.myName}   계좌 {this.numbers}   개설일 {this.myDate}   잔액 {this.money}원");
        }

        public void Withdraw()
        {
            Console.WriteLine($"출금금 계좌 정보: 이름 {this.myName}   계좌 {this.numbers}   잔액 {this.money}원");
            Console.Write("입금할 금액 입력: ");

            string tempMoney = Console.ReadLine();
            int subMoney = Convert.ToInt32(tempMoney);
            if (this.money < subMoney)
            {
                this.money = 0;
            }
            else
            {
                this.money -= subMoney;
            }
        }

    }

    class System : Account
    {
        //public static string[] member_list = new string[numberL-1];
        public static string[] member_list = new string[numberL-1];


        public static void trans()
        {
            Console.Write("송금할 계좌번호 입력 : ");
            string temp_number = Console.ReadLine();
            Console.Write("송금할 금액 입력 : ");
            string temp_money = Console.ReadLine();
        }
    }

    class CustomBank
    {
        static void Main()
        {
            Account bank1 = new Account();
            bank1.PrintMy();

            Account bank2 = new Account();
            bank2.PrintMy();
            
            Account bank3 = new Account();
            bank3.PrintMy();

        }
    }
}

*/




// delegate 대리자
// 대리자는 매개변수 목록 및 반환 형식이 있는 메서드 참조를 나타내는 형식이다.
// 함수 기능을 호출하는 개념으로 사용된다.

// 대리자는 delegate 키워드를 사용해서 만들 수 있다.
// 대리자는 함수 자체를 하나의 데이터로 보고 다른 메서드를 실행하는 기능이다.
// 한 번에 메서드 하나 이상을 대신해서 호출할 수 있다.

// 메서드의 매개변수로 대리자 변수(개체)를 넘길 수 있다.
// 대리자를 사용하여 함수의 매개변수로 함수 자체를 전달할 수 있다.
// 대리자는 동일한 메서드 시그니처를 갖는 메서드 참조를 담는 그릇 역할
// 대리자를 사용하면 함수를 모아 놓았다가 나중에 실행하거나 실행을 취소할 수 있다.
// 대리자는 앞에 배울 이벤트를 만들어 내는 중간 단계의 작업이다.



// 이벤트
// 이벤트는 특정 상황이 발생할 때 객체 또는 클래스에서 알림을 제공할 수 있도록 하는 멤버로
// 버튼 클릭, 마우스 오버 등 같은 이벤트 기반 프로그래밍에 사용되는 개념
// 콘솔앱은 마우스 클릭 X
// 데스크톱앱 윈도우앱에서 자주 사용
// event 키워드를 사용한다.

// 사건 사고 등 의미 : 프로그래밍에서는 함수 실행되는 결과를 의미
// 이벤트 : 클릭과 마우스 오버 같은 동작 자체
// 이벤트 처리기 : 특정 이벤트를 담당하기 위해 만든 메서드


// 이벤트와 대리자를 사용해서 메서드 등록 및 호출하기
// 대리자는 이벤트를 위한 중간 단계이다.
// 이벤트는 메서드 여러 개를 등록한 후 실행시키는 역할
// 운영체제 레벨에서마우스 및 키보드 등 장치와 연동할 때 이벤트를 사용한다.





// 클래스 - 부분(분할 클래스 partial class
// 클래스의 기능이 많아 클래스 규모가 커지면 클래스를 나눌 수 있음
// 분할 클래스 방식으로 역할 분담 가능
// 컴파일시 하나의 클래스로 처리
// 분할 클래스들을 클래스명


/*
// 클래스의 상속
// 클래스간 부모 자식 관계를 설정해서 상속 가능
// 상속은 부모클래스에 정의된 기능을 다시 사용하거나 확장 / 수정하여 자식 클래스를 만드는 것
// 상속하는 방법

// public class A
// {
//      A클래스의 코드
// }

// public class B : A
// {
//      A를 상속 받은 B 클래스의 코드
// }


// System.Object 클래스는 닷넷 모든 클래스의 부모 클래스이다.
// 새롭게 만드는 모든 클래스는 System.Object 클래스를 상속받아 만드는 것

// 기본 base 클래스 : 부모클래스를 의미
// 파생 derived 클래스 : 다른 클래스의 자식 클래스가 되는 클래스를 파생클래스라고 함. 혹은 sub클래스 라고 함

// 부모클래스와 자식 클래스
// 클론 : 기호로 상속 관계를 지정하면 부모 클래스와 public 멤버들을 자식 클래스에서 그대로 물려받아 사용 가능
// public, protected 사용 가능
// 

 
*/

/*
// this 키워드
// 클래스 내에서 this는 자신을 의미하고, this() : 자신의 생성자를 나타냄
// base 키워드
// base 는 자신의 부모클래스를 의미
// base() : 부모클래스의 생성자
 */

namespace ConstructorParameter
{
    public class ParentClass : Object
    {
        public ParentClass(string message) => Console.WriteLine(message);
        protected void Print1() => Console.WriteLine("부모클래스의 함수");
    }

    public class ChildClass : ParentClass
    {
        public ChildClass(string message) : base(message) { }
        public void Print2() => base.Print1();
    }

    class Demo
    {
        static void Main()
        {
            //ParentClass p = new ParentClass();
            //Console.WriteLine(p.ToString());

            //ChildClass c = new ChildClass();
            //c.Print2();
            ////ParentClass.Print1();     // 오류 : protected 로 감싸져 있어 외부에서 접근 불가

            string msg = "매개변수";
            var child = new ChildClass(msg);
        }
    }




/*
    class Parent
    {
        public void AA() => Console.WriteLine("parent_AA");
        public override string ToString()   // 부모클래스의 함수를 덮어쓰기 override
        {
            return "부모클래스 tostring";
        }
    }
    class Child : Parent
    {
        public void BB() => Console.WriteLine("Child_BB");
        public override string ToString()
        {
            return "자식클래스 tostring";
        }
    }

    class Demo
    {
        static void Main()
        {
            var child = new Child();
            Console.WriteLine(child.ToString());
            child.AA();
            child.BB();
        }
    }
 */


    /*
    class PartialClassDemo
    {
        static void Main()
        {
            var hello = new Hello();
            hello.Hi();
            hello.Bye();    // 인스턴스 생성 후 두 개로 나뉜 partial 클래스 내부 멤버에 접근 가능
            // 부분 클래스(분할 클래스를 사용하여 CS파일 하나 또는 하나 이상에서 이름이 동일한 클래스 개발 가능
        }
    }
    */

    /*
    public partial class Person
    {
        public string Name { get; set; }
        public int age { get; set; }

    }
    public partial class Person
    {
        public void Print() => Console.WriteLine($"{Name} : {age}");
    }
    
    class PartialClass
    {
        static void Main()
        {
            Person person = new Person();
            person.Name = "학생1";
            person.age = 10;
            person.Print();
        }
    }
     */


    //public class ButtonClass
    //{
    //    public delegate void EventHandler();    // 이벤트 핸들러라는 대리자 생성
    //    public event EventHandler Click;        // 클릭이라는 이름의 이벤트 생성, event 키워드와 대리자 형식을 함께 사용
    //    public void Onclick()   // Click 이벤트에 등록된 메서드가 있다면 이벤트가 호출되는 함수
    //    {
    //        if (Click != null)  // 이벤트에 함수가 등록되어있는지 검사
    //        {
    //            Click();
    //        }
    //    }
    //}
    //class CunstructorParameter
    //{
    //    static void Main()
    //    {
    //        ButtonClass btn = new ButtonClass();    // 위 buttonclass의 인스턴스 생성
    //        btn.Click += Hi1;   // btn 인스턴스의 click 이벤트에 함수 등록
    //        btn.Click += Hi2;
    //        btn.Onclick();  // btn 인스턴스의 Onclick 함수 호출
    //    }

    //    static void Hi1() => Console.WriteLine("hi1 호출");
    //    static void Hi2() => Console.WriteLine("hi2 호출");
    //}




    //static void Hi() => Console.WriteLine("Hi");    // 함수 Hi 생성
    //delegate void SayDelegate();    // 대리자 생성
    //static void Main()
    //{
    //    SayDelegate say = Hi;   // 함수를 데이터로 보고 say라는 식별자의 대리자 개체에 Hi 지정
    //    say();      // hi라는 함수의 호출을 대리자 say를 통해 호출 가능, 대리자를 통한 함수 호출
    //    // 위 코드처럼 이미 있는 함수(Hi)를 대신 호출하는 개념이 대리자의 목적이다.
    //    // 대리자 변수 = new 대리자(메서드 이름);
    //    // 대리자 변수 += new 대리자 (메서드 이름);      형태로 사용 사능
    //}



    //delegate void SayPointer();     
    //// delegate 키워드를 사용해서 void SayPointer()로 매개변수 및 반환 값이 없는 메서드를 대신 호출하는 대리자 생성

    //static void Hello() => Console.WriteLine("hello");
    //// 대리자에 담아 대신 호출할 hello 메서드 선언

    //static void Main()
    //{
    //    SayPointer saypointer = new SayPointer(Hello);  
    //    // saypointer라는 식별자를 가진 SayPointer 인스턴스를 만들고 생성자 대신 실행할 메서드 이름을 지정하는 방식으로 대리자 객체 생성

    //    saypointer();           // 호출방식 1 : 대리자 변수에 괄호를 붙여 호출
    //    saypointer.Invoke();    // 호출방식 2 : 대리자에 invoke 함수를 통한 호출   == 명시적 호출
    //}



    //delegate void SayDelegate();
    //static void Main()
    //{
    //    SayDelegate say = delegate ()       // 익며메서드 혹은 무명메서드 방식으로 delegate 지정
    //    {
    //        Console.WriteLine("Delegate");
    //    };

    //    say();  // 호출
    //}



    //public class CarDriver
    //{
    //    public static void GoForward() => Console.WriteLine("앞");
    //    public static void GoBackward() => Console.WriteLine("뒤");
    //    public static void GoLeft() => Console.WriteLine("좌");
    //    public static void GoRight() => Console.WriteLine("우");
    //}

    //public class Insa
    //{
    //    public void Bye() => Console.WriteLine("잘가");
    //}

    //public delegate void GoHome();

    //class ConstructorParameter
    //{
    //    public delegate void Say();
    //    private static void Hello() { Console.WriteLine("hello"); }
    //    private static void Hi() { Console.WriteLine("hi"); }
    //    static void Main()
    //    {
    //        CarDriver.GoForward();
    //        CarDriver.GoBackward();
    //        CarDriver.GoLeft();
    //        CarDriver.GoRight();

    //        GoHome go = new GoHome(CarDriver.GoForward);
    //        go += new GoHome(CarDriver.GoRight);
    //        go += new GoHome(CarDriver.GoRight);
    //        go += new GoHome(CarDriver.GoRight);
    //        go += new GoHome(CarDriver.GoRight);
    //        go += new GoHome(CarDriver.GoRight);
    //        go -= new GoHome(CarDriver.GoRight);
    //        go();


    //        Say say;
    //        say = new Say(Hi);
    //        say += new Say(Hello);
    //        say();


    //        Insa insa = new Insa();
    //        Say say2 = new Say(insa.Bye);
    //        say2 += new Say(insa.Bye);
    //        say2();
    //    }
    //}



    //public class Print
    //{
    //    public static void Show(string message) { Console.WriteLine(message); }
    //}
    //class ConstructorParameter
    //{
    //    public delegate void PrintDelegate(string message);
    //    public delegate void SumDelegate(int a, int b);
    //    public delegate void Lambda();
    //    public delegate int Lambda2(int i);
    
    //    static void Main()
    //    {
    //        Print.Show("매개변수텍스트");
    //        PrintDelegate pd = new PrintDelegate(Print.Show);
    //        pd("pd매개변수텍스트");

    //        PrintDelegate am = delegate (string message)
    //        {
    //            Console.WriteLine(message);
    //        };
    //        am("am익명함수 매개변수 텍스트");
        
    //        SumDelegate sd = delegate (int a, int b) { Console.WriteLine(a + b); };
    //        sd(10, 30);

    //        Lambda hi = () => Console.WriteLine("Lambda람다 호출");     // 람다 형식으로 함수 선언
    //        hi();

    //        Lambda2 square = x => x * x;        // 매개변수와 반환값이 있는 람다식
    //        Console.WriteLine(square(3));
    //    }

    //}


    //class ConstructorParameter
    //{
    //    public delegate void Runner();
    //    static void Main()
    //    {
    //        RunnerCall(new Runner(Go));
    //        RunnerCall(new Runner(Back));
    //    }

    //    static void RunnerCall(Runner runner) => runner();  // 대리자를 매개변수로 전달
    //    static void Go() => Console.WriteLine("앞");
    //    static void Back() => Console.WriteLine("뒤");
    //}


}