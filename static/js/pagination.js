jQuery(document).ready(function($){
  $('.channel-pagination-block').paginathing({
    perPage: 4,
    limitPagination: 3,
    prevText:'<i class="fa-solid fa-angle-left"></i>' ,
    nextText:'<i class="fa-solid fa-angle-right"></i>' ,
    firstText: '<i class="fa-solid fa-angles-left"></i>',
    lastText: '<i class="fa-solid fa-angles-right"></i>',
    pageNumbers: true,
  })
});