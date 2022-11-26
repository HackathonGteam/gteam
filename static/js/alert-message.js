

function alertMessage(){
  // メッセージ内容を取得
  let message = document.getElementById("message").value;
  // アラートフラグ
  let alertFlg = false;
  
  // メッセージ内容に不適切用語が存在するかを確認
  alertFlg = alertCheck(message);
  // 不適切なワードが入っていた場合
  if(alertFlg) {
    alert('不適切なワードが入っています。投稿内容を確認してください');
    return false;

  // 上記以外の場合
  } else {
    doucument.messageForm.submit();
  }
}

function alertIndex(){
  // メッセージ内容を取得
  let channelName = document.getElementById("channelName").value;
  // アラートフラグ
  let alertFlg = false;
  
  // メッセージ内容に不適切用語が存在するかを確認
  alertFlg = alertCheck(channelName);
  // 不適切なワードが入っていた場合
  if(alertFlg) {
    alert('不適切なワードが入っています。投稿内容を確認してください');
    return false;

  // 上記以外の場合
  } else {
    doucument.messageForm.submit();
  }
}

//alertCheck機能
function alertCheck(message) {
  const badMessages = ["バカ", "クソ", "死ね", "〇ね", "馬鹿", "はげ", "禿", "ハゲ", "〇げ"]
  // アラートフラグの初期化
  let alertFlg = false;

  for (let i = 0; i < badMessages.length; i++) {
    let badM = badMessages[i]
    if(message.indexOf(badM) != -1) {
      alertFlg = true;
      break;
    }
  }
  return alertFlg;
}
