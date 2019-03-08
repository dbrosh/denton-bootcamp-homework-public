Sub StockDataEasy()
    
    'Declare Values'
    
    Dim Ticker As String
    Dim TotalVolume As Double
    TotalVolume = 0
    Dim TVRow As Integer
    TVRow = 2
    Dim ws As Worksheet
    
        'Create a worksheet loop'
        For Each ws In Worksheets
        
        'Place titles in each sheet for calculated data'
        ws.Cells(1, "I") = "Ticker"
        ws.Cells(1, "J") = "Total Volume"
    
        LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
            'Loop Through Stock Data'
    
            For i = 2 To LastRow
    
                'Determine id Ticker is Same'
                 If ws.Cells(i + 1, 1).Value <> ws.Cells(i, 1).Value Then
    
                 'If not create new Ticker'
                Ticker = ws.Cells(i, 1).Value
    
                'Total Trading Volume'
                TotalVolume = TotalVolume + ws.Cells(i, 7).Value
    
                'Print Ticker in Column I'
                ws.Range("I" & TVRow).Value = Ticker
    
                'Print Total Volume in Column J'
                ws.Range("J" & TVRow).Value = TotalVolume
    
                'Create new row for each unique Ticker'
                TVRow = TVRow + 1
    
                'Reset Total Volume to 0'
                TotalVolume = 0
    
    
                Else
    
                'Add to Total Volume'
                TotalVolume = TotalVolume + ws.Cells(i, 7).Value
    
                End If
    
            Next i
    
        'Reset Total Volume Row to 2 for each worksheet'
        TVRow = 2
        
        Next ws
       
End Sub
