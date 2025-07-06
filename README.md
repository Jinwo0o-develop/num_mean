# num_mean
당연히 기초지만, 평균을 구하는 프로그램을 작성할겁니다 !<br>
2개, 3개, 일반화까지 가능하다면 좋겠네여.<br>
<br>
### 숫자 2개로 만들어보기
![image](https://github.com/user-attachments/assets/5dc16fbc-bf7c-4cde-ac2e-7e7e453fc623)<br>
저번에 배운 input을 사용해서 입력받았는데, 시작부터 사소한 실수를 했습니다.<br>
사칙연산 우선순위를 고려하지 않아서 a+(b/2)가 되어버렸고, (a+b)/2로 수정했어요.<br>
이때부터 오늘 고생할 걸 알았어야했는데...<br>
<br>
### 숫자 3개로 만들어보기 및 가독성 확보
![image](https://github.com/user-attachments/assets/b779d90e-cf8d-4b3c-b80b-d96f295ade2e)<br>
복사붙여넣기를 하다보니 print에 두 숫자를 입력하라고 되어있더라구요.<br>
처음엔 몰랐는데 이 쯤에서 알 수 있는게, 간단하다고 사소하게 넘어가버리면 실수가 생긴다는걸 알았습니다.<br>
반드시, 고쳐야 할 단점이겠더라구요.<br>
## 관심 포인트 체인지
이제 len함수를 사용하지 않고, sum/3 에서 3을 변수의 개수로써 바꾸고 싶더라구요.<br>
4가지 방법이 떠올랐습니다.<br>
**편하게 len 사용하기**  **반복문 사용하기**<br>
**함수를 만들어서 해결**  **클래스로 해결**<br>
당연히 사서 고생하는 편이 실력에 도움된다고 생각하기에 함수와 클래스를 채택했습니다.<br>
그래야 이해 안된 부분도 찾을 수 있고 나중에 당황도 안하고 사고가 유연해지더라구요.<br>
![image](https://github.com/user-attachments/assets/06374340-90f6-4b68-8a3f-e755bfa44613)<br>
작성하기 무섭게 UnboundLocalError라고 떳습니다. 숫자를 카운팅할 변수 n을 함수안에 넣고 밖에 빼고 해도 똑같더라구요. <br>
![image](https://github.com/user-attachments/assets/eb4a6793-f241-4877-936e-c24532daaa85)<br>
전역변수와 지역변수의 개념을 이해하고 n을 밖에 뺏는데도 오류가 나왔습니다.<br>
왜 오류가 나는지 처음에는 몰랐지만, 일단 안되니까 n = 0, count = n + 1, 이런 변수도 해서 return count를 사용하기도 했습니다.<br>
![image](https://github.com/user-attachments/assets/123ce64b-8dd4-4a30-b42a-b1c23d540de1)<br>
일단, 뭘 해도 안되니 큰 뼈대부터 잡아놓고, 계속 쪼물쪼물 건드려봤는데 이건 또 되더라구요 ?<br>
![image](https://github.com/user-attachments/assets/e41f97ae-a208-43f9-aa89-f93118344f48)<br>
???? 일단 단세포인 머리로 이해하긴 어려워보이니 gpt한테 달려갔습니다.<br>
일단, 함수바깥에 선언하면 전역변수가 맞고, 안에 선언하면 지역변수인게 맞다.<br>
이 코드가 되는 이유는 count를 안에서 수정이나 새로 선언하는 것이 아닌, 읽기만 하기 떄문이다, 즉 읽기만 하면 전역변수로써 유지된다. 그래서 문제가 없는 것이고,<br>
반대로, 바꾸려고 하면 지역 변수로 간주하는 것. 해결할려면 global 함수를 사용해야 한다고 하는데, 일단 내 능력 껏 해보기로 했다.<br>
대신 언젠간 도움이 될테니 나중에 꼭 해봐야겠어.<br>
![image](https://github.com/user-attachments/assets/bf4ee5bc-79e0-462c-a09a-7ce591f692cf)<br>
함수 자체가 호출되는걸 보고, 변수에 저장하는 아이디어를 찾아냈습니다.
![image](https://github.com/user-attachments/assets/fd11cc79-e9c2-4fa7-8143-755d5c5e5e8e)<br>
정말 이때부터 많이많이 고민했습니다.. 이 부분에서 2시간정도 고민했는데, 짚이는 대로 문제점도 고민해봤는데, 해결방법이 떠오르질 않으니 답답하더라구요.
a가 1이나 2로 고정되기도 하고, 이 쯤에서 global이라는 걸 까먹어버려서 결국 GPT한테 물어보러 갔습니다.
**상황설명**
![image](https://github.com/user-attachments/assets/d9a057a4-7e4a-4ebf-a147-c8717e93c3d3)<br>
"변수를 함수 외부에 정의하거나, 함수 외부에서 누적시키는 방법을 사용해야 숫자 개수를 셀 수 있어요."
이걸 보고도 이해가 안가서 집요하게 물어보다가 global 말고 다른 방법 없냐고 물어보니 CLASS로 푸는 방법을 말하더라구요?
그래서 그냥 CLASS로 옮겨서 풀어버렸습니다.
지금보니 그냥 global해보고 클래스로 넘어가지 왜 애매하게 저랬나 싶네요


다음에는, global 함수 사용과 gpt에게 반복문을 사용하지 않고 방법이 없냐고 물어보니 재귀함수를 이용한 방법이 있다고 하길래 사용해볼겁니다.
