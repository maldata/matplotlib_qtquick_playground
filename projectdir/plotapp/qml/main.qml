import QtQuick 2.6
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

ApplicationWindow
{
    title: qsTr("Plot Test App")
    width: 640
    height: 480
    color: "whitesmoke"

    onClosing: main.shutdown()

    ColumnLayout
    {
        id: mainLayout
        anchors.fill: parent
        spacing: 16

        Label {
            id: status
            text: "Label"
            Layout.margins: 5
        }

	Button {
	    id: button
	    text: "Btn"
	    onClicked: main.shutdown()
	}

    }  // ColumnLayout
}  // ApplicationWindow
