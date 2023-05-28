let check = document.getElementById("basic-form");
    check.addEventListener("submit", (e) => {
        let stock = document.getElementById("stocks");
        if(stock.value.length === 0){
            alert("종목을 입력하세요");
            e.preventDefault();
        }
    })