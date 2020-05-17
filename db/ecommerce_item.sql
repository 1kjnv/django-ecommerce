-- MySQL dump 10.13  Distrib 8.0.12, for macos10.13 (x86_64)
--
-- Host: localhost    Database: ecommerce
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `price` int(11) DEFAULT NULL,
  `description` longtext NOT NULL,
  `color` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  `category` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `item_created_by_id_f892047e_fk_auth_user_id` (`created_by_id`),
  CONSTRAINT `item_created_by_id_f892047e_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES (15,'Macbook pro',1999,'Macbook Pro 2017 Touch bar version','Grey','images/macbook_pro.jpeg',5,'2020-05-04 08:57:22.121324',5,'Electronics'),(16,'Dell Alienware',1950,'Alienware is the best laptop model for all students and software developers','Blue','images/dell.jpg',3,'2020-05-04 12:11:28.701362',5,'Electronics'),(17,'iMac',2499,'iMac Desktop computer with high performance for home based atmosphere','Silver','images/iMac.jpg',5,'2020-05-04 12:16:34.942748',5,'Electronics'),(18,'Men T-shirt',30,'Nike tshirt for men','Black','images/nike.jpg',5,'2020-05-04 12:48:37.781900',5,'Men Clothes'),(19,'Nike 2 for men',23,'Nike Tshirt for men for summer season','Black','images/nike2.jpg',6,'2020-05-04 12:51:09.108663',5,'Men Clothes'),(20,'Women Dress #1',90,'Long dress for women for summer','Red','images/women-clothes-1_HmsvPOT.jpg',5,'2020-05-04 12:51:55.099311',5,'Women Clothes'),(21,'Women Dress #2',145,'Long and soft material clothes for summer season for women','Blue','images/women-2.jpg',5,'2020-05-04 12:52:45.887739',5,'Women Clothes'),(22,'Face Mask',15,'Face cream for women. It helps women to soften their skins','Silver','images/cream.jpg',10,'2020-05-04 12:56:04.097275',5,'Beauty'),(23,'Educated',18,'Educated is the #1 \"The New York Times\" best-seller since 2018. ','Red','images/educated_zQzJgad.jpg',3,'2020-05-04 12:57:02.660833',5,'Books'),(24,'Women Shoes #1',59,'Women shoes for this season','Red','images/women-shoes-1.jpg',4,'2020-05-04 12:58:37.583714',5,'Shoes'),(25,'Women Shoes #2',99,'Women shoes for this season #2','Grey','images/women-shoes-2.jpg',5,'2020-05-04 12:59:14.819252',5,'Shoes'),(26,'Macbook Air',1399,'Macbook Air 2017 version','Silver','images/mac_air.jpg',6,'2020-05-05 09:26:17.838128',5,'Electronics'),(27,'iPhone SE 2',399,'iPhone SE 2 new model of Apple products. The latest product!','Black','images/iphone.jpeg',2,'2020-05-08 13:38:02.775767',5,'Electronics');
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-17 17:20:13
