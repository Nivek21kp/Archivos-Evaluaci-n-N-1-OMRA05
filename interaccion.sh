#Script que permite la ejecucion de archivos y cambia propiedad a ROOT

#Kevin Pacheco Linco

#Permite Ejecucion de archivo
chmod +x $1

#Cambia la propiedad del archivo a root 
sudo chown root:root $1

echo "Se ha cambiado la propiedad del archivo"
