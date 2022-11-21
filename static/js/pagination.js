jQuery(document).ready(function($){
  $('.channel-pagination-block').paginathing({
    perPage: 4,
    firstLast: false,
    prevText:'prev' ,
    nextText:'next' ,
    activeClass: 'active',
  })
});