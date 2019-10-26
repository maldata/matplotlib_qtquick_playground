import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Layouts 1.3

import "../styles"

Rectangle {
    color: "whitesmoke"

    ColumnLayout {
	anchors.fill: parent

	Label {
            text: "This page intentionally left blank!"
	}

	Item {
	    Layout.fillHeight: true
	}
    }
}
