private fun uploadFileToRenderServer(file: File) {
    Thread {
        try {
            val boundary = "----Boundary${System.currentTimeMillis()}"
            val url = URL("https://你的網址.onrender.com/upload")
            val conn = url.openConnection() as HttpURLConnection
            conn.requestMethod = "POST"
            conn.doOutput = true
            conn.setRequestProperty("Content-Type", "multipart/form-data; boundary=$boundary")

            val output = conn.outputStream
            val writer = output.bufferedWriter()

            // Part 1: filename field
            writer.write("--$boundary\r\n")
            writer.write("Content-Disposition: form-data; name=\"filename\"\r\n\r\n")
            writer.write(file.name + "\r\n")

            // Part 2: file content
            writer.write("--$boundary\r\n")
            writer.write("Content-Disposition: form-data; name=\"file\"; filename=\"${file.name}\"\r\n")
            writer.write("Content-Type: text/plain\r\n\r\n")
            writer.flush()
            output.write(file.readBytes())

            // End boundary
            output.write("\r\n--$boundary--\r\n".toByteArray())
            output.flush()

            val responseCode = conn.responseCode
            runOnUiThread {
                if (responseCode == 200) {
                    Toast.makeText(this, "已上傳至 GitHub", Toast.LENGTH_SHORT).show()
                } else {
                    Toast.makeText(this, "上傳失敗：$responseCode", Toast.LENGTH_SHORT).show()
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }.start()
}
