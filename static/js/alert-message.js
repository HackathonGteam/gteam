// 送信時にメッセージのチェックを行う
document.messageForm.btn.addEventListener('click', function() {

  // メッセージ内容を取得
  var message = document.getElementById("message").value;
  // アラートフラグ
  var alertFlg = false;
  
  // メッセージ内容に不適切用語が存在するかを確認
  for (var i = 0; i < badMessages.length; i++) {
    var badM = badMessages[i]
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

var badMessages = ["バカ", "クソ", "死ね"]