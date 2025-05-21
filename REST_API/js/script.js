const apiUrl = "https://api.escuelajs.co/api/v1/products";
const productList = document.getElementById("productList");

// Hàm lấy và hiển thị danh sách sản phẩm
function fetchAndRenderProducts() {
    // Gọi API để lấy danh sách sản phẩm
    //- Get dùng để lấy dữ liêu như (lấy danh sách sinh viên). mặc định khi gọi API là GET
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            // Xóa danh sách cũ trước khi render mới
            productList.innerHTML = ""; 
            data.forEach(product => {
                const productCard = document.createElement("div");
                productCard.classList.add("product");
                productCard.innerHTML = `
                    <img src="${product.images[0]}" alt="${product.title}" />
                    <h3>${product.title}</h3>
                    <p>Giá: $${product.price}</p>
                    <p>${product.description}</p>
                    <button class="btn btn-primary delete-btn">Xóa</button>
                    <button class="btn btn-secondary edit-btn">chỉnh sửa</button>
                `;
                // Thêm sự kiện cho nút chỉnh sửa
                productCard.querySelector('.edit-btn').addEventListener('click', function() {
                    document.getElementById("productName").value = product.title;
                    document.getElementById("productPrice").value = product.price;
                    document.getElementById("productDescription").value = product.description;
                    document.getElementById("productImage").value = product.images[0];
                    // Nếu có trường categoryId, bạn có thể điền vào đây
                    editingProductId = product.id;
                    document.getElementById("addProductButton").textContent = "Cập nhật sản phẩm";
                });
                //Thêm sự kiện cho nút xóa
                productCard.querySelector('.delete-btn').addEventListener('click', function() {
                    if (confirm("Bạn có chắc chắn muốn xóa sản phẩm này?")) {
                        deleteProduct(product.id);
                    }
                });
                productList.appendChild(productCard);
            });
        })
        .catch(error => {
            productList.innerHTML = "<p>Không thể tải sản phẩm. Vui lòng thử lại sau.</p>";
            console.error("Lỗi khi gọi API:", error);
        });
}
// Hàm thêm sản phẩm mới dùng method POST
function addProduct(newProduct) {
    //- POST dùng để thêm dữ liệu mới vào server như (thêm sản phẩm)
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
// Hàm cập nhật sản phẩm dùng method PUT
function updateProduct(productId, updatedProduct) {
    //- PUT dùng để cập nhật dữ liệu đã có trên server như (cập nhật sản phẩm)
    fetch(`${apiUrl}/${productId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        }, 
        body: JSON.stringify(updatedProduct),})
    .then(response => response.json())
    .then(data => {
        console.log("Sản phẩm đã được cập nhật:", data);
        fetchAndRenderProducts();
    })
    .catch(error => {
        console.error("Lỗi khi cập nhật sản phẩm:", error);
    });
}
// Hàm xóa sản phẩm
function deleteProduct(productId){
    //- DELETE dùng để xóa dữ liệu trên server như (xóa sản phẩm)
    fetch(`${apiUrl}/${productId}`, {
        method: "DELETE",
        headers:{
            "Content-Type": "application/json",
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log("Sản phẩm đã được xóa:", data);
            // Cập nhật lại danh sách sản phẩm
            fetchAndRenderProducts();
        })
        .catch(error => {
            console.error("Lỗi khi xóa sản phẩm:", error);
        });
}
// Gọi hàm để tải và hiển thị danh sách sản phẩm khi trang được tải
fetchAndRenderProducts();
// Thêm sự kiện cho nút thêm sản phẩm/ cập nhật sản phẩm
let editingProductId = null;
document.getElementById("addProductForm").addEventListener("submit", function (event) {
    event.preventDefault();
    const productData = {
        title: document.getElementById("productName").value,
        price: Number(document.getElementById("productPrice").value),
        description: document.getElementById("productDescription").value,
        categoryId: Number(document.getElementById("productCategory").value),
        images: [document.getElementById("productImage").value],
    };
    if (editingProductId) {
        updateProduct(editingProductId, productData);
        editingProductId = null;
    } else {
        addProduct(productData);
    }
    event.target.reset();
});
