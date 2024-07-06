const all_cookie = [
]

async function clear_cookies() {
    all_cookie.forEach((el) => {
        deleteCookie(el);
    })
    console.log(deleteCookie)
}
await clear_cookies();


alert(document.cookie); // показываем все куки
