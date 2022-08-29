Attribute VB_Name = "progressBar"
Sub progressBar()
    Dim objFond As Shape
    Dim objBarre As Shape


        Const sLongueurPourcent As Single = 0.25 '% de  la longueur de la diapo (0.25 =>25%)
        Const sHauteurPourcent As Single = 0.015 '% de  la hauteur de la diapo
        Const sPositionXPourcent As Single = 0.63 '% de  la longueur de la diapo en partant de la gauche
        Const sPositionYPourcent As Single = 0.035  '% de  la hauteur de la diapo en partant du bas


        On Error Resume Next
            With ActivePresentation
                nbSlides = (.Slides.Count - 2)
                For X = 2 To nbSlides
                    .Slides(X).Shapes("PB").Delete
                    .Slides(X).Shapes("PBF").Delete

                    Set objFond = .Slides(X).Shapes.AddShape(msoShapeRoundedRectangle, .PageSetup.SlideWidth * (1 - sPositionXPourcent), .PageSetup.SlideHeight * (1 - sPositionYPourcent), .PageSetup.SlideWidth * sLongueurPourcent, .PageSetup.SlideHeight * sHauteurPourcent)
                    objFond.Adjustments.Item(1) = 0.5 'Arete en arrondi
                    objFond.Line.Weight = 1
                    objFond.Fill.ForeColor.RGB = RGB(255, 255, 255) 'Couleur du fond
                    objFond.Name = "PBF"

                    Set objBarre = .Slides(X).Shapes.AddShape(msoShapeRoundedRectangle, .PageSetup.SlideWidth * (1 - sPositionXPourcent), .PageSetup.SlideHeight * (1 - sPositionYPourcent), X * .PageSetup.SlideWidth * sLongueurPourcent / nbSlides, .PageSetup.SlideHeight * sHauteurPourcent)
                    objBarre.Adjustments.Item(1) = 0.5 'Arete en arrondi
                    objBarre.Line.Weight = 1
                    objBarre.Fill.TwoColorGradient msoGradientHorizontal, 1
                    objBarre.Fill.GradientStops.Insert RGB(255, 0, 0), 0 'Point de dégradé 1 : couleur et position (0%)
                    objBarre.Fill.GradientStops.Insert RGB(240, 0, 0), 0.5 'Point de dégradé 2 : couleur et position
                    objBarre.Fill.GradientStops.Insert RGB(190, 0, 0), 1 'Point de dégradé 3 : couleur et position (100%)
                    objBarre.Name = "PB"
                Next
            End With
End Sub
