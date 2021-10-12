function generateQRCode() {
	eel.generate_qr()
}
function getPathToFile() {
    eel.fileSave()(r => console.log(r));
};