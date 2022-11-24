const deleteBtn = document.getElementById('delete-btn');

deleteBtn.addEventListener('click', function(e) {
  let result = window.confirm('削除してもよろしいですか？');
    
  if( result ) {
      
  } else {
    e.preventDefault();
  }
})