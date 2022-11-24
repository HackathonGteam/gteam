const updateButton = document.getElementById("channel-update");
const updateChannelModal = document.getElementById("update-channel-modal");
const updatePageButtonClose = document.getElementById("update-page-close-btn");
const updateForm = document.getElementById("updateForm");
const channelName = document.getElementById("channelName");

const updateChannel = () => {
  if (userId !== channel.USER_ID) {
    return;
  } else {
    modalOpen();
  }
};

function btnUpdate(){
  if (channelName.value == null || channelName.value == "") {
    alert("チャンネル名を入力してください");
    return false;
  } else {
    updateForm.method = "POST";
    updateForm.action = "/update_channel";
    updateForm.submit();
  }
}

updateButton.addEventListener("click", updateChannel);

updatePageButtonClose.addEventListener("click", () => {
  modalClose("update");
});



function modalOpen() {
  updateChannelModal.style.display = "block";
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == updateChannelModal) {
    updateChannelModal.style.display = "none";
  }
}

function modalClose() {
  updateChannelModal.style.display = "none";
}
