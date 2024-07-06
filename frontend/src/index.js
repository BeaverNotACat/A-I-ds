cookie_labels = [
  "gender",
  "age_from",
  "age_to",
  "income",
  "avaliable_banners"
]

function clear_cookies() {
  cookie_labels.forEach(element => {
    deleteCookie(element);
  });
}