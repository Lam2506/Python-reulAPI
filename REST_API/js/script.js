const apiUrl = "https://api.escuelajs.co/api/v1/products";
const productList = document.getElementById("productList");

// Hàm lấy và hiển thị danh sách sản phẩm
function fetchAndRenderProducts() {
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            productList.innerHTML = ""; // Xóa danh sách cũ trước khi render mới
            data.forEach(product => {
                const productCard = document.createElement("div");
                productCard.classList.add("product");
                productCard.innerHTML = `
                    <img src="${product.images[0]}" alt="${product.title}" />
                    <h3>${product.title}</h3>
                    <p>Giá: $${product.price}</p>
                `;
                productList.appendChild(productCard);
            });
        })
        .catch(error => {
            productList.innerHTML = "<p>Không thể tải sản phẩm. Vui lòng thử lại sau.</p>";
            console.error("Lỗi khi gọi API:", error);
        });
}
function addProduct(newProduct) {
    fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newProduct),
    })
    .then(response => response.json())
    .then(data => {
        console.log("Sản phẩm mới đã được thêm:", data);
        // Cập nhật lại danh sách sản phẩm
        fetchAndRenderProducts();
    })
    .catch(error => {
        console.error("Lỗi khi thêm sản phẩm:", error);
    });
}

// Gọi hàm để tải và hiển thị danh sách sản phẩm khi trang được tải
fetchAndRenderProducts();
// Thêm sự kiện cho nút thêm sản phẩm
document.getElementById("addProductForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Ngăn form gửi lại và reload trang
    const newProduct = {
        title: document.getElementById("productName").value,
        price: Number(document.getElementById("productPrice").value),
        description: document.getElementById("productDescription").value,
        images: [document.getElementById("productImage").value],
        categoryId: 1 // Thêm dòng này, chọn ID phù hợp với API
    };

    addProduct(newProduct);
});