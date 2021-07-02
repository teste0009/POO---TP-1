-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.25 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para ecommerce
CREATE DATABASE IF NOT EXISTS `ecommerce` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `ecommerce`;

-- Volcando estructura para tabla ecommerce.carritos
CREATE TABLE IF NOT EXISTS `carritos` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_usuario` int unsigned NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `b_comprado` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.carritos: ~5 rows (aproximadamente)
/*!40000 ALTER TABLE `carritos` DISABLE KEYS */;
INSERT INTO `carritos` (`id`, `id_usuario`, `total`, `b_comprado`) VALUES
	(8, 2, 1008.00, 1),
	(9, 2, 394.99, 1),
	(10, 2, 822.00, 1),
	(11, 3, 849.00, 1),
	(13, 3, 992.00, 1),
	(14, 4, 5699.95, 1),
	(15, 2, 1135.00, 0);
/*!40000 ALTER TABLE `carritos` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.categorias: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` (`id`, `nombre`) VALUES
	(1, 'Motherboards'),
	(2, 'Procesadores'),
	(3, 'Memorias'),
	(4, 'Placas de Video');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.ciudades
CREATE TABLE IF NOT EXISTS `ciudades` (
  `id` int unsigned NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `id_provincia` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ciudad_provincia` (`id_provincia`),
  CONSTRAINT `ciudad_provincia` FOREIGN KEY (`id_provincia`) REFERENCES `provincias` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.ciudades: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` (`id`, `nombre`, `id_provincia`) VALUES
	(1, 'CABA', 1),
	(2, 'Rosario', 5),
	(3, 'Santa Rosa', 8),
	(12, 'Carmelo', 75),
	(15, 'Montevideo', 77),
	(71, 'Barcelona', 96);
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.compras
CREATE TABLE IF NOT EXISTS `compras` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_carrito` int unsigned NOT NULL,
  `id_producto` int unsigned NOT NULL,
  `cantidad` int unsigned NOT NULL,
  `sub_total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_carrito` (`id_carrito`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `id_carrito` FOREIGN KEY (`id_carrito`) REFERENCES `carritos` (`id`),
  CONSTRAINT `id_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.compras: ~14 rows (aproximadamente)
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` (`id`, `id_carrito`, `id_producto`, `cantidad`, `sub_total`) VALUES
	(21, 8, 3, 2, 168.00),
	(22, 8, 2, 1, 740.00),
	(23, 8, 4, 1, 100.00),
	(24, 9, 5, 1, 195.00),
	(25, 9, 6, 1, 199.99),
	(26, 10, 1, 1, 570.00),
	(28, 11, 3, 1, 84.00),
	(29, 11, 1, 1, 570.00),
	(30, 11, 5, 1, 195.00),
	(34, 10, 3, 3, 252.00),
	(35, 13, 3, 3, 252.00),
	(36, 13, 2, 1, 740.00),
	(37, 14, 4, 5, 500.00),
	(38, 14, 2, 5, 3700.00),
	(39, 14, 6, 5, 999.95),
	(40, 14, 4, 5, 500.00),
	(41, 15, 4, 2, 200.00),
	(42, 15, 5, 1, 195.00),
	(43, 15, 2, 1, 740.00);
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.marcas: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`id`, `nombre`) VALUES
	(1, 'Asus'),
	(2, 'Msi'),
	(3, 'Gigabyte'),
	(4, 'Asrock'),
	(5, 'Intel'),
	(6, 'Amd'),
	(7, 'Thermaltake'),
	(8, 'Kingston');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.paises
CREATE TABLE IF NOT EXISTS `paises` (
  `id` int NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.paises: ~4 rows (aproximadamente)
/*!40000 ALTER TABLE `paises` DISABLE KEYS */;
INSERT INTO `paises` (`id`, `nombre`) VALUES
	(34, 'España'),
	(49, 'Alemania'),
	(54, 'Argentina'),
	(598, 'Uruguay');
/*!40000 ALTER TABLE `paises` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `id_categoria` int unsigned NOT NULL,
  `id_marca` int unsigned NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_categoria` (`id_categoria`),
  KEY `id_marca` (`id_marca`),
  CONSTRAINT `id_categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id`),
  CONSTRAINT `id_marca` FOREIGN KEY (`id_marca`) REFERENCES `marcas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.productos: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`id`, `id_categoria`, `id_marca`, `nombre`, `precio`) VALUES
	(1, 4, 4, 'Radeon RX 570 4Gb', 570.00),
	(2, 4, 1, 'GeForce GTX 1660 6Gb', 740.00),
	(3, 3, 8, 'DDR4 - 8 Gb 2666 Mhz Value', 84.00),
	(4, 3, 7, 'DDR4 - 8 Gb 3000Mhz H-one', 100.00),
	(5, 2, 6, 'Ryzen 5 3600 4.2 Ghz - AM4', 195.00),
	(6, 2, 5, 'Core i5 10400F 4.3 Ghz', 199.99);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.provincias
CREATE TABLE IF NOT EXISTS `provincias` (
  `id` int NOT NULL,
  `nombre` varchar(255) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `id_pais` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `provincia_pais` (`id_pais`),
  CONSTRAINT `provincia_pais` FOREIGN KEY (`id_pais`) REFERENCES `paises` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.provincias: ~6 rows (aproximadamente)
/*!40000 ALTER TABLE `provincias` DISABLE KEYS */;
INSERT INTO `provincias` (`id`, `nombre`, `id_pais`) VALUES
	(1, 'Buenos Aires', 54),
	(5, 'Santa Fé', 54),
	(8, 'La Pampa', 54),
	(75, 'Colonia', 598),
	(77, 'Montevideo', 598),
	(96, 'Cataluña', 34);
/*!40000 ALTER TABLE `provincias` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `dni` int unsigned NOT NULL,
  `nombre` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `id_ciudad` int unsigned NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci NOT NULL,
  `b_admin` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `id_ciudad` (`id_ciudad`),
  CONSTRAINT `id_ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudades` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_spanish_ci;

-- Volcando datos para la tabla ecommerce.usuarios: ~3 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`id`, `dni`, `nombre`, `id_ciudad`, `email`, `password`, `b_admin`) VALUES
	(1, 12345678, 'Admin', 1, 'admin@email.com', 'YWRtaW4=', 1),
	(2, 22354687, 'Enzo', 1, 'enzo@gmail.com', 'X0hvbGExMjM=', 0),
	(3, 33465798, 'Nicolás', 2, 'nico@gmail.com', 'X0hvbGExMjM=', 0),
	(4, 48567234, 'Lionel', 71, 'leo10@gmail.com', 'QW50b18xMA==', 0),
	(5, 123456, 'Shazam', 15, 'shazam@hotmail.com', 'X0hvbGExMjM=', 0);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
