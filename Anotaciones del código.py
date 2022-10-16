#Órbita (planet.py, line 37): Dibujar la órbita más atrás (no que empiece dibujandose con el cuerpo celeste) para que no se provoque
        #el efecto visual de que la orbita se dibujó y luego se movió (len>15), sino que para que la animación comience
        #de inmediato en movimiento, ya que el trazo extra de órbita dibujado anticipadamente se comenzaría a pintar
        #de negro inmediatamente (len>2), no se busca pintar de negro inmediatamente sin haber dibujado la órbita más atrás
        #ya que no daría tiempo para que se cree la cola de la órbita y, por tanto, el efecto de movimiento.

#

#

#
#Acerca del cambio de velocidad utilizando TIMESTEP
https://stackoverflow.com/questions/13950266/restricted-3-body-simulation-not-working-correctly

#Esta órbita se cruza con las demás
https://gizmodo.com/the-amazing-hypothesis-for-why-the-trappist-1-system-ha-1795089833


