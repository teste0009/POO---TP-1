import mysql.connector
import base64


_db_config = {
  'host': 'localhost',
  'port': '3306',
  'user': 'root',
  'password': 'root',
  'database':'ecommerce'
}

class Db():
  def __init__(self) -> None:
    self.conexion = mysql.connector.Connect(**_db_config)
    self.cursor = self.conexion.cursor()
    self.__sql = {
      "id_pais": "select id from paises where nombre=%s",
      "id_provincia": "select id from provincias where nombre=%s and id_pais=%s",
      "id_ciudad": "select id from ciudades where nombre=%s and id_provincia=%s",
      "get_email": "select email from usuarios where email=%s",
      "get_login": ("select us.*, ci.nombre as ciudad, pr.nombre as provincia, pa.nombre as pais "
                  "from usuarios us "
                  "left join ciudades ci on us.id_ciudad = ci.id "
                  "left join provincias pr on ci.id_provincia = pr.id "
                  "left join paises pa on pr.id_pais = pa.id "
                  "where email = %s and password = %s"),
      "insert_usuario": "insert into usuarios (dni, nombre, id_ciudad, email, password, b_admin) values (%s, %s, %s, %s, %s, 0)",
      "get_productos": ("select pr.id, ca.nombre, ma.nombre, pr.nombre, pr.precio "
                        "from productos pr "
                        "left join categorias ca on ca.id = pr.id_categoria "
                        "left join marcas ma on ma.id = pr.id_marca "
                        "order by ca.nombre, ma.nombre, pr.nombre"),
      "insert_carrito": "insert into carritos (id_usuario, total) values (%s, %s)",
      "insert_compra": "insert into compras (id_carrito, id_producto, cantidad, sub_total) values (%s, %s, %s, %s)",
      "get_carrito": "select id, total from carritos where id_usuario=%s and b_comprado=0 limit 1",
      "get_compras": ("select co.id, co.cantidad, concat(ma.nombre, ' ', pr.nombre) as descripcion, co.sub_total "
                      "from compras co "
                      "left join productos pr on pr.id=co.id_producto "
                      # "left join categorias ca on ca.id=pr.id_categoria "
                      "left join marcas ma on ma.id=pr.id_marca "
                      "where id_carrito=%s"),
      "update_total_carrito": "update carritos set total=(select ifnull(sum(sub_total), 0) from compras where id_carrito=%s) where id=%s limit 1",
      "get_total_carrito": "select total from carritos where id=%s limit 1",
      "borrar_compra": "delete from compras where id=%s limit 1",
      "borrar_carrito": "delete from carritos where id=%s limit 1",
      "finalizar_compra": "update carritos set b_comprado=1 where id=%s limit 1",
      "get_carritos_usuario": "select b_comprado, count(id) as cantidad, ifnull(sum(total), 0) as total from carritos where id_usuario=%s group by b_comprado",
      "get_categorias": "select * from categorias order by nombre",
      "get_marcas": "select * from marcas order by nombre",
      "get_usuarios":  ("select u.*, convert(from_base64(password), nchar) as pass_decode, if(b_admin=1, 'SI', 'NO') AS admin, "
                          "c.nombre as ciudad, p.nombre as provincia, pa.nombre as pais "
                        "from usuarios u "
                        "left join ciudades c on u.id_ciudad = c.id "
                        "left join provincias p on c.id_provincia = p.id "
                        "left join paises pa on p.id_pais = pa.id "),
      "get_resumen_carritos":  ("select us.nombre, if(ca.b_comprado=1, 'SI', 'NO') as finalizado, count(distinct(ca.id)) as carritos, "
                                  "ifnull(sum(co.sub_total), 0) as total, sum(co.cantidad) as productos "
                                "from carritos ca "
                                "left join usuarios us on us.id=ca.id_usuario "
                                "left join compras co on co.id_carrito=ca.id "
                                "group by ca.id_usuario, ca.b_comprado "
                                "order by us.nombre, ca.b_comprado desc "),
    }

  def get_cursor(self):
    return self.cursor

  def get_conexion(self):
    return self.conexion

  def encode_pass(self, password):
    return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8').strip()

  def __decode_pass(self,password):
    return base64.decodebytes(password.encode("UTF-8")).decode('utf-8')

  def get_fetchone(self, sql_ind, _val=tuple):
    self.get_cursor().execute(self.__sql[sql_ind], _val)
    return self.get_cursor().fetchone()

  def get_fetchall(self, sql_ind, _val=None):
    self.get_cursor().execute(self.__sql[sql_ind], _val)
    return self.get_cursor().fetchall()

  def commit(self, sql_ind, _val=None):
    self.get_cursor().execute(self.__sql[sql_ind], _val)
    self.get_conexion().commit()

  def get_lastrowid(self, sql_ind, _val=None):
    self.commit(sql_ind, _val)
    return self.get_cursor().lastrowid

  def get_rowcount(self, sql_ind, _val=None):
    self.commit(sql_ind, _val)
    return self.get_cursor().rowcount

  def get_id(self, sql_ind, _val=tuple) -> int:
    _valor_id = self.get_fetchone(sql_ind, _val)
    return 0 if (_valor_id == None) else _valor_id[0]

_dbi=Db()
