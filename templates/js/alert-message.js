// 送信時にメッセージのチェックを行う
document.messageForm.btn.addEventListener('click', function() {

  // メッセージ内容を取得
  let message = document.getElementById("message").value;
  // アラートフラグ
  let alertFlg = false;
  
  // メッセージ内容に不適切用語が存在するかを確認
  for (let i = 0; i < badMessages.length; i++) {
    let badM = badMessages[i]
    if(message.indexOf(badM) != -1) {
      alertFlg = true;
      break;
    }
  }
  if(alertFlg) {
    var result = confirm('相手を傷つける言葉が含まれている可能性があります。本当に送信しますか？');
    // "OK"/"キャンセル"により分岐
    if( result ) {
      // "OK"を選択したとき
      doucument.messageForm.submit();
    } else {
      // "キャンセル"を選択したとき
      document.getElementById("message").value = "";
      window.location.reload();
    }
  } else {
    doucument.messageForm.submit();
  }
  
})

const badMessages = ["バカ", "クソ", "死ね", "〇ね", "馬鹿", "はげ", "禿", "ハゲ", "〇げ"]