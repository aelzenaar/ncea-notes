set table "notes.pgf-plot.table"; set format "%.5f"
set format "%.7e";; set contour base; set cntrparam levels discrete 0.003; unset surface; set view map; set isosamples 100; set samples 100; splot x**3 + y**4 - 5*x*y + 2*x; 
