#!/usr/bin/env python

from xmlschemaparser import from_wsdl_file
from cStringIO import StringIO

# The source below is from http://webservices.amazon.com/AWSECommerceService/AWSECommerceService.wsdl
Parser = from_wsdl_file(StringIO("""<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://schemas.xmlsoap.org/wsdl/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://webservices.amazon.com/AWSECommerceService/2009-11-01" targetNamespace="http://webservices.amazon.com/AWSECommerceService/2009-11-01">
    <types>
		<xs:schema targetNamespace="http://webservices.amazon.com/AWSECommerceService/2009-11-01" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:tns="http://webservices.amazon.com/AWSECommerceService/2009-11-01" elementFormDefault="qualified">
	
	        <xs:element name="Bin">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element name="BinName" type="xs:string" />
	                                <xs:element name="BinItemCount" type="xs:positiveInteger" />
	                                <xs:element name="BinParameter" minOccurs="0" maxOccurs="unbounded">
		                              <xs:complexType>
	                                          <xs:sequence>
	                                                 <xs:element name="Name" type="xs:string" />
	                                                 <xs:element name="Value" type="xs:string" />
	                                          </xs:sequence>
	                                      </xs:complexType>
	                                </xs:element>
	                        </xs:sequence>
	                </xs:complexType>
	        </xs:element>
	        <xs:element name="SearchBinSet">
	                <xs:complexType>
	                        <xs:sequence>
	                               <xs:element ref="tns:Bin" minOccurs="0" maxOccurs="unbounded" />
	                        </xs:sequence>
	                        <xs:attribute name="NarrowBy" type="xs:string" use="required" />
	                </xs:complexType>
	        </xs:element>
		<xs:element name="SearchBinSets">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element ref="tns:SearchBinSet" minOccurs="0" maxOccurs="unbounded" />
	                        </xs:sequence>
	                </xs:complexType>
	        </xs:element>
		<xs:element name="Help">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:HelpRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:HelpRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="HelpRequest">
			<xs:sequence>
				<xs:element name="About" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="HelpType" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="Operation"/>
							<xs:enumeration value="ResponseGroup"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="ItemSearch">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/> 
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
	            			<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:ItemSearchRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:ItemSearchRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="ItemSearchRequest">
			<xs:sequence>
				<xs:element name="Actor" type="xs:string" minOccurs="0"/>
	      			<xs:element name="Artist" type="xs:string" minOccurs="0"/>
				<xs:element name="Availability" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="Available"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element ref="tns:AudienceRating" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="Author" type="xs:string" minOccurs="0"/>
				<xs:element name="Brand" type="xs:string" minOccurs="0"/>
				<xs:element name="BrowseNode" type="xs:string" minOccurs="0"/>
				<xs:element name="City" type="xs:string" minOccurs="0"/>
				<xs:element name="Composer" type="xs:string" minOccurs="0"/>
				<xs:element ref="tns:Condition" minOccurs="0"/>
				<xs:element name="Conductor" type="xs:string" minOccurs="0"/>
				<xs:element name="Count" type="xs:positiveInteger" minOccurs="0">
					<xs:annotation>
						<xs:appinfo>
							<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
								<aws-se:excludeFrom>public</aws-se:excludeFrom>
								<aws-se:excludeFrom>partner</aws-se:excludeFrom>
							</aws-se:restricted>
						</xs:appinfo>
					</xs:annotation>
				</xs:element>
				<xs:element name="Cuisine" type="xs:string" minOccurs="0"/>
				<xs:element ref="tns:DeliveryMethod" minOccurs="0"/>
				<xs:element name="Director" type="xs:string" minOccurs="0"/>
	                        <xs:element name="FutureLaunchDate" type="xs:string" minOccurs="0"/>
	                        <xs:element name="ISPUPostalCode" type="xs:string" minOccurs="0"/>
				<xs:element name="ItemPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="Keywords" type="xs:string" minOccurs="0"/>
				<xs:element name="Manufacturer" type="xs:string" minOccurs="0"/>
				<xs:element name="MaximumPrice" type="xs:nonNegativeInteger" minOccurs="0"/>
				<xs:element name="MerchantId" type="xs:string" minOccurs="0"/>
				<xs:element name="MinimumPrice" type="xs:nonNegativeInteger" minOccurs="0"/>
				<xs:element name="MusicLabel" type="xs:string" minOccurs="0"/>
				<xs:element name="Neighborhood" type="xs:string" minOccurs="0"/>
				<xs:element name="Orchestra" type="xs:string" minOccurs="0"/>
				<xs:element name="PostalCode" type="xs:string" minOccurs="0"/>
				<xs:element name="Power" type="xs:string" minOccurs="0"/>
				<xs:element name="Publisher" type="xs:string" minOccurs="0"/>
				<xs:element name="RelatedItemPage" type="tns:positiveIntegerOrAll" minOccurs="0"/>
				<xs:element name="RelationshipType" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ReviewSort" type="xs:string" minOccurs="0"/>
				<xs:element name="SearchIndex" type="xs:string" minOccurs="0"/>
				<xs:element name="Sort" type="xs:string" minOccurs="0"/>
				<xs:element name="State" type="xs:string" minOccurs="0"/>
				<xs:element name="TagPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagsPerPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagSort" type="xs:string" minOccurs="0"/>
				<xs:element name="TextStream" type="xs:string" minOccurs="0"/>
				<xs:element name="Title" type="xs:string" minOccurs="0"/>
				<xs:element name="ReleaseDate" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="ItemLookup">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:ItemLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:ItemLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="ItemLookupRequest">
			<xs:sequence>
				<xs:element ref="tns:Condition" minOccurs="0"/>
				<xs:element ref="tns:DeliveryMethod" minOccurs="0"/>
	                        <xs:element name="FutureLaunchDate" type="xs:string" minOccurs="0"/>
	                        <xs:element name="IdType" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="ASIN"/>
							<xs:enumeration value="UPC"/>
							<xs:enumeration value="SKU"/>
							<xs:enumeration value="EAN"/>
							<xs:enumeration value="ISBN"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="ISPUPostalCode" type="xs:string" minOccurs="0"/>
				<xs:element name="MerchantId" type="xs:string" minOccurs="0"/>
				<xs:element name="OfferPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="ItemId" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ReviewPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="ReviewSort" type="xs:string" minOccurs="0"/>
				<xs:element name="SearchIndex" type="xs:string" minOccurs="0"/>
				<xs:element name="SearchInsideKeywords" type="xs:string" minOccurs="0">
					<xs:annotation>
						<xs:appinfo>
							<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
								<aws-se:excludeFrom>public</aws-se:excludeFrom>
								<aws-se:excludeFrom>partner</aws-se:excludeFrom>
							</aws-se:restricted>
						</xs:appinfo>
					</xs:annotation>
				</xs:element>
				<xs:element name="TagPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagsPerPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagSort" type="xs:string" minOccurs="0"/>
				<xs:element name="VariationPage" type="tns:positiveIntegerOrAll" minOccurs="0"/>
				<xs:element name="RelatedItemPage" type="tns:positiveIntegerOrAll" minOccurs="0"/>
				<xs:element name="RelationshipType" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="ListSearch">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:ListSearchRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:ListSearchRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="ListSearchRequest">
			<xs:sequence>
				<xs:element name="City" type="xs:string" minOccurs="0"/>
				<xs:element name="Email" type="xs:string" minOccurs="0"/>
				<xs:element name="FirstName" type="xs:string" minOccurs="0"/>
				<xs:element name="LastName" type="xs:string" minOccurs="0"/>
				<xs:element name="ListPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="ListType">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="WishList"/>
							<xs:enumeration value="WeddingRegistry"/>
							<xs:enumeration value="BabyRegistry"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="Name" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="State" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="ListLookup">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:ListLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:ListLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="ListLookupRequest">
			<xs:sequence>
				<xs:element ref="tns:Condition" minOccurs="0"/>
				<xs:element ref="tns:DeliveryMethod" minOccurs="0"/>
				<xs:element name="ISPUPostalCode" type="xs:string" minOccurs="0"/>
				<xs:element name="ListId" type="xs:string" minOccurs="0"/>
				<xs:element name="ListType" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="WishList"/>
							<xs:enumeration value="Listmania"/>
							<xs:enumeration value="WeddingRegistry"/>
							<xs:enumeration value="BabyRegistry"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="MerchantId" type="xs:string" minOccurs="0"/>
				<xs:element name="ProductGroup" type="xs:string" minOccurs="0"/>
				<xs:element name="ProductPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ReviewSort" type="xs:string" minOccurs="0"/>
				<xs:element name="Sort" type="xs:string" minOccurs="0"/>
				<xs:element name="IsOmitPurchasedItems" type="xs:boolean" minOccurs="0"/>
				<xs:element name="IsIncludeUniversal" type="xs:boolean" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CustomerContentSearch">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CustomerContentSearchRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CustomerContentSearchRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CustomerContentSearchRequest">
			<xs:sequence>
				<xs:element name="CustomerPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="Email" type="xs:string" minOccurs="0"/>
				<xs:element name="Name" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CustomerContentLookup">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CustomerContentLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CustomerContentLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CustomerContentLookupRequest">
			<xs:sequence>
				<xs:element name="CustomerId" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ReviewPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagsPerPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagSort" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="SimilarityLookup">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:SimilarityLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:SimilarityLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="SimilarityLookupRequest">
			<xs:sequence>
				<xs:element ref="tns:Condition" minOccurs="0"/>
				<xs:element ref="tns:DeliveryMethod" minOccurs="0"/>
				<xs:element name="ItemId" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ISPUPostalCode" type="xs:string" minOccurs="0"/>
				<xs:element name="MerchantId" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ReviewSort" type="xs:string" minOccurs="0"/>
				<xs:element name="SimilarityType" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="Intersection"/>
							<xs:enumeration value="Random"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="SellerLookup">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:SellerLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:SellerLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="SellerLookupRequest">
			<xs:sequence>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="SellerId" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="FeedbackPage" type="xs:positiveInteger" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CartGet">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CartGetRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CartGetRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CartGetRequest">
			<xs:sequence>
				<xs:element name="CartId" type="xs:string" minOccurs="0"/>
				<xs:element name="HMAC" type="xs:string" minOccurs="0"/>
				<xs:element name="MergeCart" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CartAdd">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CartAddRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CartAddRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CartAddRequest">
			<xs:sequence>
				<xs:element name="CartId" type="xs:string" minOccurs="0"/>
				<xs:element name="HMAC" type="xs:string" minOccurs="0"/>
				<xs:element name="MergeCart" type="xs:string" minOccurs="0"/>
				<xs:element name="Items" minOccurs="0">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="Item" minOccurs="0" maxOccurs="unbounded">
								<xs:complexType>
									<xs:sequence>
										<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
										<xs:element name="OfferListingId" type="xs:string" minOccurs="0"/>
										<xs:element name="Quantity" type="xs:positiveInteger" minOccurs="0"/>
										<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
										<xs:element name="ListItemId" type="xs:string" minOccurs="0"/>
										<xs:element name="MetaData" minOccurs="0" maxOccurs="unbounded">
											<xs:complexType>
												<xs:sequence>
													<xs:element name="Key" type="xs:string" minOccurs="0"/>
													<xs:element name="Value" type="xs:string" minOccurs="0"/>
												</xs:sequence>
											</xs:complexType>
										</xs:element>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CartCreate">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CartCreateRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CartCreateRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CartCreateRequest">
			<xs:sequence>
				<xs:element name="MergeCart" type="xs:string" minOccurs="0"/>
				<xs:element name="Items" minOccurs="0">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="Item" minOccurs="0" maxOccurs="unbounded">
								<xs:complexType>
									<xs:sequence>
										<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
										<xs:element name="OfferListingId" type="xs:string" minOccurs="0"/>
										<xs:element name="Quantity" type="xs:positiveInteger" minOccurs="0"/>
										<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
										<xs:element name="ListItemId" type="xs:string" minOccurs="0"/>
										<xs:element name="MetaData" minOccurs="0" maxOccurs="unbounded">
											<xs:complexType>
												<xs:sequence>
													<xs:element name="Key" type="xs:string" minOccurs="0"/>
													<xs:element name="Value" type="xs:string" minOccurs="0"/>
												</xs:sequence>
											</xs:complexType>
										</xs:element>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CartModify">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CartModifyRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CartModifyRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CartModifyRequest">
			<xs:sequence>
				<xs:element name="CartId" type="xs:string" minOccurs="0"/>
				<xs:element name="HMAC" type="xs:string" minOccurs="0"/>
				<xs:element name="MergeCart" type="xs:string" minOccurs="0"/>
				<xs:element name="Items" minOccurs="0">
					<xs:complexType>
						<xs:sequence>
							<xs:element name="Item" minOccurs="0" maxOccurs="unbounded">
								<xs:complexType>
									<xs:sequence>
										<xs:element name="Action" minOccurs="0">
											<xs:simpleType>
												<xs:restriction base="xs:string">
													<xs:enumeration value="MoveToCart"/>
													<xs:enumeration value="SaveForLater"/>
												</xs:restriction>
											</xs:simpleType>
										</xs:element>
										<xs:element name="CartItemId" type="xs:string" minOccurs="0"/>
										<xs:element name="Quantity" type="xs:nonNegativeInteger" minOccurs="0"/>
									</xs:sequence>
								</xs:complexType>
							</xs:element>
						</xs:sequence>
					</xs:complexType>
				</xs:element>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="CartClear">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:CartClearRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:CartClearRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CartClearRequest">
			<xs:sequence>
				<xs:element name="CartId" type="xs:string" minOccurs="0"/>
				<xs:element name="HMAC" type="xs:string" minOccurs="0"/>
				<xs:element name="MergeCart" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="TransactionLookup">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:TransactionLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:TransactionLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="TransactionLookupRequest">
			<xs:sequence>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="TransactionId" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="SellerListingSearch">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:SellerListingSearchRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:SellerListingSearchRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="SellerListingSearchRequest">
			<xs:sequence>
				<xs:element name="Keywords" type="xs:string" minOccurs="0"/>
				<xs:element name="ListingPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="OfferStatus" minOccurs="0">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="Open"/>
							<xs:enumeration value="Closed"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="SellerId" type="xs:string" minOccurs="1"/>
				<xs:element name="Sort" type="xs:string" minOccurs="0"/>
				<xs:element name="Title" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="SellerListingLookup">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:SellerListingLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:SellerListingLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TagLookup">
			<xs:complexType>
				<xs:sequence>
	            			<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:TagLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:TagLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="SellerListingLookupRequest">
			<xs:sequence>
				<xs:element name="Id" type="xs:string"/>
	                        <xs:element name="SellerId" type="xs:string" minOccurs="0"/>
				<xs:element name="IdType">
					<xs:simpleType>
						<xs:restriction base="xs:string">
							<xs:enumeration value="Exchange"/>
							<xs:enumeration value="Listing"/>
	                                                <xs:enumeration value="ASIN"/>
	                                                <xs:enumeration value="SKU"/>
						</xs:restriction>
					</xs:simpleType>
				</xs:element>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:complexType name="TagLookupRequest">
			<xs:sequence>
				<xs:element name="TagName" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="CustomerId" type="xs:string" minOccurs="0"/>
				<xs:element name="TagPage" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="Count" type="xs:positiveInteger" minOccurs="0"/>
				<xs:element name="TagSort" type="xs:string" minOccurs="0"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="BrowseNodeLookup">
			<xs:complexType>
				<xs:sequence>
		        	    	<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/> 
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:BrowseNodeLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:BrowseNodeLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="BrowseNodeLookupRequest">
			<xs:sequence>
				<xs:element name="BrowseNodeId" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="VehicleSearch">
			<xs:complexType>
				<xs:sequence>
		        	    	<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:VehicleSearchRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:VehicleSearchRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="VehicleSearchRequest">
			<xs:sequence>
				<xs:element name="Year" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="MakeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="ModelId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="TrimId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="VehiclePartSearch">
			<xs:complexType>
				<xs:sequence>
		        	    	<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/> 
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:VehiclePartSearchRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:VehiclePartSearchRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="VehiclePartSearchRequest">
			<xs:sequence>
				<xs:element name="Year" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="MakeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="ModelId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="TrimId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BedId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BodyStyleId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BrakesId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="DriveTypeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="EngineId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="MfrBodyCodeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="SpringTypesId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="SteeringId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="TransmissionId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="WheelbaseId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BrowseNodeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Brand" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Count" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="FromItemId" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="PartPageDirection" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="VehiclePartLookup">
			<xs:complexType>
				<xs:sequence>
		        	    	<xs:element name="MarketplaceDomain" type="xs:string" minOccurs="0"/>
					<xs:element name="AWSAccessKeyId" type="xs:string" minOccurs="0"/> 
					<xs:element name="SubscriptionId" type="xs:string" minOccurs="0"/>
					<xs:element name="AssociateTag" type="xs:string" minOccurs="0"/>
					<xs:element name="Validate" type="xs:string" minOccurs="0"/>
					<xs:element name="XMLEscaping" type="xs:string" minOccurs="0"/>
					<xs:element name="Shared" type="tns:VehiclePartLookupRequest" minOccurs="0"/>
					<xs:element name="Request" type="tns:VehiclePartLookupRequest" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="VehiclePartLookupRequest">
			<xs:sequence>
				<xs:element name="ItemId" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="IdType" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Year" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="MakeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="ModelId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="TrimId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BedId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BodyStyleId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BrakesId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="DriveTypeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="EngineId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="MfrBodyCodeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="SpringTypesId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="SteeringId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="TransmissionId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="WheelbaseId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BrowseNodeId" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="FitmentPage" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="FitmentCount" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
				<xs:element name="ResponseGroup" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="Condition">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="All"/>
					<xs:enumeration value="New"/>
					<xs:enumeration value="Used"/>
					<xs:enumeration value="Collectible"/>
					<xs:enumeration value="Refurbished"/>
				</xs:restriction>
			</xs:simpleType>
		</xs:element>
		<xs:element name="DeliveryMethod">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="Ship"/>
					<xs:enumeration value="ISPU"/>
				</xs:restriction>
			</xs:simpleType>
		</xs:element>
		<xs:element name="AudienceRating">
			<xs:simpleType>
				<xs:restriction base="xs:string">
					<xs:enumeration value="G"/>
					<xs:enumeration value="PG"/>
					<xs:enumeration value="PG-13"/>
					<xs:enumeration value="R"/>
					<xs:enumeration value="NC-17"/>
					<xs:enumeration value="NR"/>
					<xs:enumeration value="Unrated"/>
					<xs:enumeration value="6"/>
					<xs:enumeration value="12"/>
					<xs:enumeration value="16"/>
					<xs:enumeration value="18"/>
					<xs:enumeration value="FamilyViewing"/>
				</xs:restriction>
			</xs:simpleType>
		</xs:element>
		<xs:element name="MultiOperation">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Help" minOccurs="0"/>
					<xs:element ref="tns:ItemSearch" minOccurs="0"/>
					<xs:element ref="tns:ItemLookup" minOccurs="0"/>
					<xs:element ref="tns:ListSearch" minOccurs="0"/>
					<xs:element ref="tns:ListLookup" minOccurs="0"/>
					<xs:element ref="tns:CustomerContentSearch" minOccurs="0"/>
					<xs:element ref="tns:CustomerContentLookup" minOccurs="0"/>
					<xs:element ref="tns:SimilarityLookup" minOccurs="0"/>
					<xs:element ref="tns:SellerLookup" minOccurs="0"/>
					<xs:element ref="tns:CartGet" minOccurs="0"/>
					<xs:element ref="tns:CartAdd" minOccurs="0"/>
					<xs:element ref="tns:CartCreate" minOccurs="0"/>
					<xs:element ref="tns:CartModify" minOccurs="0"/>
					<xs:element ref="tns:CartClear" minOccurs="0"/>
					<xs:element ref="tns:TransactionLookup" minOccurs="0"/>
					<xs:element ref="tns:SellerListingSearch" minOccurs="0"/>
					<xs:element ref="tns:SellerListingLookup" minOccurs="0"/>
					<xs:element ref="tns:TagLookup" minOccurs="0"/>
					<xs:element ref="tns:BrowseNodeLookup" minOccurs="0"/>
					<xs:element ref="tns:VehicleSearch" minOccurs="0"/>
					<xs:element ref="tns:VehiclePartSearch" minOccurs="0"/>
					<xs:element ref="tns:VehiclePartLookup" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="HelpResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Information" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ItemSearchResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Items" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ItemLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Items" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ListSearchResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Lists" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ListLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Lists" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CustomerContentSearchResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Customers" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CustomerContentLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Customers" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SimilarityLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Items" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SellerLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Sellers" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CartGetResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Cart" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CartAddResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Cart" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CartCreateResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Cart" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CartModifyResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Cart" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CartClearResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Cart" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TransactionLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Transactions" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SellerListingSearchResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:SellerListings" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SellerListingLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:SellerListings" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TagLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:Tags" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="BrowseNodeLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:BrowseNodes" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleSearchResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:VehicleYears" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehiclePartSearchResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:VehicleParts" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehiclePartLookupResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:VehicleParts" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="MultiOperationResponse">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:OperationRequest" minOccurs="0"/>
					<xs:element ref="tns:HelpResponse" minOccurs="0"/>
					<xs:element ref="tns:ItemSearchResponse" minOccurs="0"/>
					<xs:element ref="tns:ItemLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:ListSearchResponse" minOccurs="0"/>
					<xs:element ref="tns:ListLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:CustomerContentSearchResponse" minOccurs="0"/>
					<xs:element ref="tns:CustomerContentLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:SimilarityLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:SellerLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:CartGetResponse" minOccurs="0"/>
					<xs:element ref="tns:CartAddResponse" minOccurs="0"/>
					<xs:element ref="tns:CartCreateResponse" minOccurs="0"/>
					<xs:element ref="tns:CartModifyResponse" minOccurs="0"/>
					<xs:element ref="tns:CartClearResponse" minOccurs="0"/>
					<xs:element ref="tns:TransactionLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:SellerListingSearchResponse" minOccurs="0"/>
					<xs:element ref="tns:SellerListingLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:TagLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:BrowseNodeLookupResponse" minOccurs="0"/>
					<xs:element ref="tns:VehicleSearchResponse" minOccurs="0"/>
					<xs:element ref="tns:VehiclePartSearchResponse" minOccurs="0"/>
					<xs:element ref="tns:VehiclePartLookupResponse" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="OperationRequest">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:HTTPHeaders" minOccurs="0"/>
					<xs:element name="RequestId" type="xs:string" minOccurs="0"/>
					<xs:element ref="tns:Arguments" minOccurs="0"/>
					<xs:element ref="tns:Errors" minOccurs="0"/>
					<xs:element name="RequestProcessingTime" type="xs:float" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Request">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="IsValid" type="xs:string" minOccurs="0"/>
					<xs:element name="HelpRequest" type="tns:HelpRequest" minOccurs="0"/>
					<xs:element name="BrowseNodeLookupRequest" type="tns:BrowseNodeLookupRequest" minOccurs="0"/>
					<xs:element name="ItemSearchRequest" type="tns:ItemSearchRequest" minOccurs="0"/>
					<xs:element name="ItemLookupRequest" type="tns:ItemLookupRequest" minOccurs="0"/>
					<xs:element name="ListSearchRequest" type="tns:ListSearchRequest" minOccurs="0"/>
					<xs:element name="ListLookupRequest" type="tns:ListLookupRequest" minOccurs="0"/>
					<xs:element name="CustomerContentSearchRequest" type="tns:CustomerContentSearchRequest" minOccurs="0"/>
					<xs:element name="CustomerContentLookupRequest" type="tns:CustomerContentLookupRequest" minOccurs="0"/>
					<xs:element name="SimilarityLookupRequest" type="tns:SimilarityLookupRequest" minOccurs="0"/>
					<xs:element name="CartGetRequest" type="tns:CartGetRequest" minOccurs="0"/>
					<xs:element name="CartAddRequest" type="tns:CartAddRequest" minOccurs="0"/>
					<xs:element name="CartCreateRequest" type="tns:CartCreateRequest" minOccurs="0"/>
					<xs:element name="CartModifyRequest" type="tns:CartModifyRequest" minOccurs="0"/>
					<xs:element name="CartClearRequest" type="tns:CartClearRequest" minOccurs="0"/>
					<xs:element name="TransactionLookupRequest" type="tns:TransactionLookupRequest" minOccurs="0"/>
					<xs:element name="SellerListingSearchRequest" type="tns:SellerListingSearchRequest" minOccurs="0"/>
					<xs:element name="SellerListingLookupRequest" type="tns:SellerListingLookupRequest" minOccurs="0"/>
					<xs:element name="SellerLookupRequest" type="tns:SellerLookupRequest" minOccurs="0"/>
					<xs:element name="TagLookupRequest" type="tns:TagLookupRequest" minOccurs="0"/>
					<xs:element name="VehicleSearchRequest" type="tns:VehicleSearchRequest" minOccurs="0"/>
					<xs:element name="VehiclePartSearchRequest" type="tns:VehiclePartSearchRequest" minOccurs="0"/>
					<xs:element name="VehiclePartLookupRequest" type="tns:VehiclePartLookupRequest" minOccurs="0"/>
					<xs:element ref="tns:Errors" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Arguments">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Argument" maxOccurs="unbounded">
						<xs:complexType>
							<xs:attribute name="Name" type="xs:string" use="required"/>
							<xs:attribute name="Value" type="xs:string"/>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="HTTPHeaders">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Header" minOccurs="0" maxOccurs="unbounded">
						<xs:complexType>
							<xs:attribute name="Name" type="xs:string" use="required"/>
							<xs:attribute name="Value" type="xs:string" use="required"/>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Errors">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Error" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Code" type="xs:string"/>
								<xs:element name="Message" type="xs:string"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Information">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element ref="tns:OperationInformation" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:ResponseGroupInformation" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Items">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element ref="tns:CorrectedQuery" minOccurs="0"/>
					<xs:element name="Qid" type="xs:string" minOccurs="0"/>
					<xs:element name="EngineQuery" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalResults" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:SearchResultsMap" minOccurs="0"/>
					<xs:element ref="tns:Item" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:SearchBinSets" minOccurs="0" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
	        <xs:element name="CorrectedQuery">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Keywords" type="xs:string" minOccurs="0"/>
					<xs:element name="Message" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Lists">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="TotalResults" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:List" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Customers">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="TotalResults" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:Customer" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Cart">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="CartId" type="xs:string"/>
					<xs:element name="HMAC" type="xs:string"/>
				        <xs:element name="URLEncodedHMAC" type="xs:string"/>
					<xs:element name="PurchaseURL" type="xs:string" minOccurs="0"/>
				        <xs:element name="SubTotal" type="tns:Price" minOccurs="0"/>
					<xs:element ref="tns:CartItems" minOccurs="0"/>
					<xs:element ref="tns:SavedForLaterItems" minOccurs="0"/>
					<xs:element ref="tns:SimilarProducts" minOccurs="0"/>
					<xs:element ref="tns:TopSellers" minOccurs="0"/>
					<xs:element ref="tns:NewReleases" minOccurs="0"/>
					<xs:element ref="tns:SimilarViewedProducts" minOccurs="0"/>
					<xs:element ref="tns:OtherCategoriesSimilarProducts" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Transactions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="TotalResults" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:Transaction" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Sellers">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="TotalResults" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:Seller" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SellerListings">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="TotalResults" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:SellerListing" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="OperationInformation">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Name" type="xs:string" minOccurs="0"/>
					<xs:element name="Description" type="xs:string" minOccurs="0"/>
					<xs:element name="RequiredParameters" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Parameter" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="AvailableParameters" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Parameter" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="DefaultResponseGroups" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ResponseGroup" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="AvailableResponseGroups" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ResponseGroup" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ResponseGroupInformation">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Name" type="xs:string" minOccurs="0"/>
					<xs:element name="CreationDate" type="xs:string" minOccurs="0"/>
					<xs:element name="ValidOperations" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Operation" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="Elements" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Element" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="List">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ListId" type="xs:string"/>
					<xs:element name="ListURL" type="xs:string" minOccurs="0"/>
					<xs:element name="RegistryNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="ListName" type="xs:string" minOccurs="0"/>
					<xs:element name="ListType" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:enumeration value="WishList"/>
								<xs:enumeration value="WeddingRegistry"/>
								<xs:enumeration value="BabyRegistry"/>
								<xs:enumeration value="Listmania"/>
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="TotalItems" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DateCreated" type="xs:string" minOccurs="0"/>
					<xs:element name="LastModified" type="xs:string" minOccurs="0"/>
					<xs:element name="OccasionDate" type="xs:string" minOccurs="0"/>
					<xs:element name="CustomerName" type="xs:string" minOccurs="0"/>
					<xs:element name="PartnerName" type="xs:string" minOccurs="0"/>
					<xs:element name="AdditionalName" type="xs:string" minOccurs="0"/>
					<xs:element name="Comment" type="xs:string" minOccurs="0"/>
					<xs:element name="Image" type="tns:Image" minOccurs="0"/>
					<xs:element name="AverageRating" type="xs:decimal" minOccurs="0"/>
					<xs:element name="TotalVotes" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalTimesRead" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:Tags" minOccurs="0"/>
					<xs:element ref="tns:ListItem" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ListItem">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ListItemId" type="xs:string" minOccurs="0"/>
					<xs:element name="DateAdded" type="xs:string" minOccurs="0"/>
					<xs:element name="Comment" type="xs:string" minOccurs="0"/>
					<xs:element name="QuantityDesired" type="xs:string" minOccurs="0"/>
					<xs:element name="QuantityReceived" type="xs:string" minOccurs="0"/>
					<xs:element name="Priority" type="xs:string" minOccurs="0"/>
					<xs:element ref="tns:Item" minOccurs="0"/>
					<xs:element ref="tns:UniversalListItem" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="UniversalListItem">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Title" type="xs:string" minOccurs="0"/>
					<xs:element name="ProductUrl" type="xs:string" minOccurs="0"/>
					<xs:element name="ImageUrl" type="xs:string" minOccurs="0"/>
					<xs:element name="SoldBy" type="xs:string" minOccurs="0"/>
					<xs:element name="SavedPrice" type="tns:Price" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Customer">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="CustomerId" type="xs:string"/>
					<xs:element name="Nickname" type="xs:string" minOccurs="0"/>
					<xs:element name="Birthday" type="xs:string" minOccurs="0"/>
					<xs:element name="WishListId" type="xs:string" minOccurs="0"/>
					<xs:element name="Location" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="UserDefinedLocation" type="xs:string" minOccurs="0"/>
								<xs:element name="City" type="xs:string" minOccurs="0"/>
								<xs:element name="State" type="xs:string" minOccurs="0"/>
								<xs:element name="Country" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element ref="tns:CustomerReviews" maxOccurs="unbounded" minOccurs="0"/>
					<xs:element ref="tns:Tags" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SearchResultsMap">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SearchIndex" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="IndexName" type="xs:string"/>
								<xs:element name="Results" type="xs:nonNegativeInteger" minOccurs="0"/>
								<xs:element name="Pages" type="xs:nonNegativeInteger" minOccurs="0"/>
								<xs:element ref="tns:CorrectedQuery" minOccurs="0"/>
								<xs:element name="RelevanceRank" type="xs:positiveInteger" minOccurs="0"/>
								<xs:element name="ASIN" type="xs:string" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Item">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ASIN" type="xs:string"/>
	                                <xs:element name="ParentASIN" type="xs:string" minOccurs="0"/>
					<xs:element ref="tns:Errors" minOccurs="0"/>
					<xs:element name="DetailPageURL" type="xs:string" minOccurs="0"/>
					<xs:element ref="tns:ItemLinks" minOccurs="0"/>
					<xs:element name="SalesRank" type="xs:string" minOccurs="0"/>
					<xs:element name="SmallImage" type="tns:Image" minOccurs="0"/>
					<xs:element name="MediumImage" type="tns:Image" minOccurs="0"/>
					<xs:element name="LargeImage" type="tns:Image" minOccurs="0"/>
					<xs:element name="ImageSets" minOccurs="0" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="MerchantId" type="xs:string" minOccurs="0" maxOccurs="1"/>
								<xs:element ref="tns:ImageSet" minOccurs="0" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element ref="tns:ItemAttributes" minOccurs="0"/>
					<xs:element ref="tns:MerchantItemAttributes" minOccurs="0"/>
					<xs:element name="VariationAttributes" minOccurs="0" maxOccurs="1">
						<xs:complexType>
							<xs:sequence>
								<xs:element ref="tns:VariationAttribute" minOccurs="0" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element ref="tns:RelatedItems" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:Collections" minOccurs="0"/>
					<xs:element name="Subjects" minOccurs="0" maxOccurs="1">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Subject" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element ref="tns:OfferSummary" minOccurs="0"/>
					<xs:element ref="tns:Offers" minOccurs="0"/>
					<xs:element ref="tns:VariationSummary" minOccurs="0"/>
					<xs:element ref="tns:Variations" minOccurs="0"/>
					<xs:element ref="tns:CustomerReviews" minOccurs="0"/>
					<xs:element ref="tns:EditorialReviews" minOccurs="0"/>
					<xs:element ref="tns:SimilarProducts" minOccurs="0"/>
					<xs:element ref="tns:Accessories" minOccurs="0"/>
					<xs:element ref="tns:Tracks" minOccurs="0"/>
					<xs:element ref="tns:BrowseNodes" minOccurs="0"/>
					<xs:element ref="tns:Tags" minOccurs="0"/>
					<xs:element ref="tns:ListmaniaLists" minOccurs="0"/>
					<xs:element ref="tns:SearchInside" minOccurs="0"/>
					<xs:element name="AlternateVersions" minOccurs="0" maxOccurs="1">
	                                  <xs:complexType>
	                                    <xs:sequence>
	                                      <xs:element name="AlternateVersion" minOccurs="0" maxOccurs="unbounded">
	                                        <xs:complexType>
	                                          <xs:sequence>
	                                            <xs:element name="ASIN" type="xs:string"/>
	                                            <xs:element name="Title" type="xs:string" minOccurs="0"/>
	                                            <xs:element name="Binding" type="xs:string" minOccurs="0"/>
	                                          </xs:sequence>
	                                        </xs:complexType>
	                                      </xs:element>
	                                    </xs:sequence>
	                                  </xs:complexType>
	                                </xs:element>
					</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ItemLinks">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:ItemLink" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ItemLink">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Description" type="xs:string" minOccurs="0"/>
					<xs:element name="URL" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
	        <xs:element name="RelatedItems">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element name="Relationship" minOccurs="0" maxOccurs="1">
	                                        <xs:simpleType>
	                                                <xs:restriction base="xs:string">
	                                                        <xs:enumeration value="Parents"/>
	                                                        <xs:enumeration value="Children"/>
	                                                </xs:restriction>
	                                        </xs:simpleType>
	                                </xs:element>
	                                <xs:element name="RelationshipType" type="xs:string" minOccurs="0" maxOccurs="1"/>
	                                <xs:element name="RelatedItemCount" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
	                                <xs:element name="RelatedItemPageCount" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
	                                <xs:element name="RelatedItemPage" type="xs:nonNegativeInteger" minOccurs="0" maxOccurs="1"/>
	                                <xs:element ref="tns:RelatedItem" minOccurs="0" maxOccurs="unbounded"/>
	                        </xs:sequence>
	                </xs:complexType>
	        </xs:element>
		<xs:element name="RelatedItem">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Item" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Tags">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="DistinctTags" type="xs:string" minOccurs="0"/>
					<xs:element name="DistinctItems" type="xs:string" minOccurs="0"/>
					<xs:element name="DistinctUsers" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalUsages" type="xs:string" minOccurs="0"/>
					<xs:element name="FirstTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element name="LastTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element ref="tns:Tag" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Tag">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Name" type="xs:string" minOccurs="0"/>
					<xs:element name="TagType" minOccurs="0">
						<xs:simpleType>
							<xs:restriction base="xs:string">
								<xs:enumeration value="Item"/>
								<xs:enumeration value="ListmaniaList"/>
								<xs:enumeration value="Guide"/>
							</xs:restriction>
						</xs:simpleType>
					</xs:element>
					<xs:element name="DistinctItems" type="xs:string" minOccurs="0"/>
					<xs:element name="DistinctUsers" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalUsages" type="xs:string" minOccurs="0"/>
					<xs:element name="FirstTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element name="LastTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element ref="tns:TaggedItems" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:TaggedListmaniaLists" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:TaggedGuides" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TaggedItems">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Item" minOccurs="0"/>
					<xs:element name="DistinctUsers" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalUsages" type="xs:string" minOccurs="0"/>
					<xs:element name="FirstTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element name="LastTagging" type="tns:Tagging" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TaggedListmaniaLists">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:List" minOccurs="0"/>
					<xs:element name="DistinctUsers" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalUsages" type="xs:string" minOccurs="0"/>
					<xs:element name="FirstTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element name="LastTagging" type="tns:Tagging" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TaggedGuides">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Guide" minOccurs="0"/>
					<xs:element name="DistinctUsers" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalUsages" type="xs:string" minOccurs="0"/>
					<xs:element name="FirstTagging" type="tns:Tagging" minOccurs="0"/>
					<xs:element name="LastTagging" type="tns:Tagging" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Guide">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="GuideId" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="Tagging">
			<xs:sequence>
				<xs:element name="Name" type="xs:string" minOccurs="0"/>
				<xs:element name="EntityId" type="xs:string" minOccurs="0"/>
				<xs:element name="UserId" type="xs:string" minOccurs="0"/>
				<xs:element name="Time" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="OfferSummary">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="LowestNewPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="LowestUsedPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="LowestCollectiblePrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="LowestRefurbishedPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="TotalNew" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalUsed" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalCollectible" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalRefurbished" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Offers">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TotalOffers" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalOfferPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:Offer" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Offer">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Merchant" minOccurs="0"/>
					<xs:element ref="tns:Seller" minOccurs="0"/>
					<xs:element ref="tns:OfferAttributes" minOccurs="0"/>
					<xs:element ref="tns:OfferListing" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:LoyaltyPoints" minOccurs="0"/>
					<xs:element ref="tns:Promotions" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="OfferAttributes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Condition" type="xs:string" minOccurs="0"/>
					<xs:element name="SubCondition" type="xs:string" minOccurs="0"/>
	 				<xs:element name="ConditionNote" type="xs:string" minOccurs="0"/>
	                                <xs:element name="WillShipExpedited" type="xs:boolean" minOccurs="0"/>
	                                <xs:element name="WillShipInternational" type="xs:boolean" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Merchant">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MerchantId" type="xs:string"/>
					<xs:element name="Name" type="xs:string" minOccurs="0"/>
					<xs:element name="GlancePage" type="xs:string" minOccurs="0"/>
	                                <xs:element name="Location" minOccurs="0">
	                                        <xs:complexType>
	                                                <xs:sequence>
	                                                        <xs:element name="CountryCode" type="xs:string" minOccurs="0"/>
	                                                        <xs:element name="StateCode" type="xs:string" minOccurs="0"/>
	                                                </xs:sequence>
	                                        </xs:complexType>
	                                </xs:element>
	                                <xs:element name="AverageFeedbackRating" type="xs:decimal" minOccurs="0"/>
	                                <xs:element name="TotalFeedback" type="xs:nonNegativeInteger" minOccurs="0"/>
	                                <xs:element name="TotalFeedbackPages" type="xs:nonNegativeInteger" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="OfferListing">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="OfferListingId" type="xs:string" minOccurs="0"/>
					<xs:element name="ExchangeId" type="xs:string" minOccurs="0"/>
					<xs:element name="Price" type="tns:Price" minOccurs="0"/>
					<xs:element name="SalePrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="AmountSaved" type="tns:Price" minOccurs="0"/>
					<xs:element name="PercentageSaved" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="Availability" type="xs:string" minOccurs="0"/>
					<xs:element name="AvailabilityAttributes" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="AvailabilityType" type="xs:string" minOccurs="0"/>
								<xs:element name="IsPreorder" type="xs:boolean" minOccurs="0"/>
								<xs:element name="MinimumHours" type="xs:integer" minOccurs="0"/>
								<xs:element name="MaximumHours" type="xs:integer" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="Quantity" type="xs:integer" minOccurs="0"/>
					<xs:element name="QuantityRestriction" minOccurs="0">
					    <xs:complexType>
							<xs:sequence>
							    <xs:element name="QuantityLimit" type="xs:integer" minOccurs="0"/>
							</xs:sequence>
					    </xs:complexType>
					</xs:element>
					<xs:element name="ISPUStoreAddress" type="tns:Address" minOccurs="0"/>
					<xs:element name="ISPUStoreHours" type="xs:string" minOccurs="0"/>
					<xs:element name="IsEligibleForSuperSaverShipping" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsEligibleForPrime" type="xs:boolean" minOccurs="0"/>
	                                <xs:element name="IsFulfilledByAmazon" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsMapViolated" type="xs:boolean" minOccurs="0"/>
	                                <xs:element name="SalesRestriction" type="xs:string" minOccurs="0"/>
	                                <xs:element name="ShippingCharge" minOccurs="0" maxOccurs="unbounded">
	                                	<xs:annotation>
	                        			<xs:appinfo>
	                                			<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
	                            					<aws-se:excludeFrom>public</aws-se:excludeFrom>
	                            					<aws-se:excludeFrom>partner</aws-se:excludeFrom>
	                            				</aws-se:restricted>
	                        		        </xs:appinfo>
	                                        </xs:annotation>
	                    			<xs:complexType>
	                        			<xs:sequence>
	                                			<xs:element name="ShippingType" type="xs:string"/>
	                                                        <xs:element name="IsRateTaxInclusive" type="xs:boolean"/>
	                                                        <xs:element name="ShippingPrice" type="tns:Price"/>
	                        			</xs:sequence>
	                                        </xs:complexType>
	                                </xs:element>
	 			</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="LoyaltyPoints">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element name="Points" type="xs:nonNegativeInteger" minOccurs="0"/>
	                                <xs:element name="TypicalRedemptionValue" type="tns:Price" minOccurs="0"/>
	                           </xs:sequence>
	                </xs:complexType>
		</xs:element>
	        <xs:element name="VariationAttribute">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element name="Name" type="xs:string"/>
	                                <xs:element name="Value" type="xs:string" maxOccurs="unbounded"/>
	                        </xs:sequence>
	                </xs:complexType>
	        </xs:element>
		<xs:element name="VariationSummary">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="LowestPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="HighestPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="LowestSalePrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="HighestSalePrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="SingleMerchantId" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Variations">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TotalVariations" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalVariationPages" type="xs:nonNegativeInteger" minOccurs="0"/>
	                                <xs:element ref="tns:VariationDimensions" minOccurs="0"/>
					<xs:element ref="tns:Item" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
	        <xs:element name="VariationDimensions">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element name="VariationDimension" type="xs:string" maxOccurs="unbounded"/>
	                        </xs:sequence>
	                </xs:complexType>
	        </xs:element>
		<xs:element name="EditorialReviews">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:EditorialReview" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Collections">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Collection" minOccurs="0" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="CollectionSummary" minOccurs="0" maxOccurs="1">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="LowestListPrice" type="tns:Price" minOccurs="0" maxOccurs="1"/>
											<xs:element name="HighestListPrice" type="tns:Price" minOccurs="0" maxOccurs="1"/>
											<xs:element name="LowestSalePrice" type="tns:Price" minOccurs="0" maxOccurs="1"/>
											<xs:element name="HighestSalePrice" type="tns:Price" minOccurs="0" maxOccurs="1"/>
										</xs:sequence>
									</xs:complexType>
								</xs:element>
								<xs:element name="CollectionParent" minOccurs="0" maxOccurs="1">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="ASIN" type="xs:string" minOccurs="0" maxOccurs="1"/>
											<xs:element name="Title" type="xs:string" minOccurs="0" maxOccurs="1"/>
										</xs:sequence>
									</xs:complexType>
								</xs:element>
								<xs:element name="CollectionItem" minOccurs="0" maxOccurs="unbounded">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="ASIN" type="xs:string" minOccurs="0" maxOccurs="1"/>
											<xs:element name="Title" type="xs:string" minOccurs="0" maxOccurs="1"/>
										</xs:sequence>
									</xs:complexType>
								</xs:element>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="EditorialReview">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Source" type="xs:string" minOccurs="0"/>
					<xs:element name="Content" type="xs:string" minOccurs="0"/>
	                                <xs:element name="IsLinkSuppressed" type="xs:boolean" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CustomerReviews">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="AverageRating" type="xs:decimal" minOccurs="0"/>
					<xs:element name="TotalReviews" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalReviewPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element ref="tns:Review" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Review">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
					<xs:element name="Rating" type="xs:decimal" minOccurs="0"/>
					<xs:element name="HelpfulVotes" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="CustomerId" type="xs:string" minOccurs="0"/>
					<xs:element ref="tns:Reviewer" minOccurs="0"/>
					<xs:element name="TotalVotes" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="Date" type="xs:string" minOccurs="0"/>
					<xs:element name="Summary" type="xs:string" minOccurs="0"/>
					<xs:element name="Content" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Reviewer">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="CustomerId" type="xs:string" minOccurs="0"/>
					<xs:element name="Name" type="xs:string" minOccurs="0"/>
					<xs:element name="Nickname" type="xs:string" minOccurs="0"/>
					<xs:element name="Location" type="xs:string" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Tracks">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Disc" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Track" maxOccurs="unbounded">
									<xs:complexType>
										<xs:simpleContent>
											<xs:extension base="xs:string">
												<xs:attribute name="Number" type="xs:positiveInteger" use="required"/>
											</xs:extension>
										</xs:simpleContent>
									</xs:complexType>
								</xs:element>
							</xs:sequence>
							<xs:attribute name="Number" type="xs:positiveInteger" use="required"/>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SimilarProducts">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SimilarProduct" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TopSellers">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TopSeller" maxOccurs="unbounded">
					<xs:complexType>
							<xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="NewReleases">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="NewRelease" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TopItemSet">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Type" type="xs:string" minOccurs="0"/>
					<xs:element name="TopItem" maxOccurs="unbounded">
	                    <xs:complexType>
	                        <xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
								<xs:element name="DetailPageURL" type="xs:string" minOccurs="0"/>
								<xs:element name="ProductGroup" type="xs:string" minOccurs="0"/>
								<xs:element name="Author" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
								<xs:element name="Artist" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
								<xs:element name="Actor" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
	                        </xs:sequence>
	                    </xs:complexType>
	                </xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SimilarViewedProducts">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SimilarViewedProduct" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="OtherCategoriesSimilarProducts">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="OtherCategoriesSimilarProduct" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Accessories">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Accessory" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
								<xs:element name="Title" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Promotions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Promotion" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Promotion">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Summary" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="PromotionId" type="xs:string"/>
								<xs:element name="Category" type="xs:string" minOccurs="0"/>
								<xs:element name="StartDate" type="xs:string" minOccurs="0"/>
								<xs:element name="EndDate" type="xs:string" minOccurs="0"/>
								<xs:element name="EligibilityRequirementDescription" type="xs:string" minOccurs="0"/>
								<xs:element name="BenefitDescription" type="xs:string" minOccurs="0"/>
								<xs:element name="TermsAndConditions" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="Details" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="MerchantId" type="xs:string"/>
								<xs:element name="OwningMerchantId" type="xs:string"/>
								<xs:element name="PromotionId" type="xs:string"/>
								<xs:element name="PromotionCategory" type="xs:string"/>
								<xs:element name="MerchantPromotionId" type="xs:string" minOccurs="0"/>
								<xs:element name="GroupClaimCode" type="xs:string" minOccurs="0"/>
								<xs:element name="CouponCombinationType" type="xs:string" minOccurs="0"/>
								<xs:element name="StartDate" type="xs:string" minOccurs="0"/>
								<xs:element name="EndDate" type="xs:string" minOccurs="0"/>
								<xs:element name="TermsAndConditions" type="xs:string" minOccurs="0"/>
								<xs:element name="EligibilityRequirements" type="tns:PromotionEligibilityRequirements" minOccurs="0"/>
								<xs:element name="Benefits" type="tns:PromotionBenefits" minOccurs="0"/>
								<xs:element name="ItemApplicability" type="tns:PromotionItemApplicability" minOccurs="0"/>
								<xs:element name="MerchandisingMessage" type="xs:string" minOccurs="0"/>
	                                                        <xs:element name="IconMediaId" type="xs:string" minOccurs="0"/>
	                                                        <xs:element name="IsIconMediaIdCustom" type="xs:boolean" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="PromotionEligibilityRequirements">
			<xs:sequence>
				<xs:element name="EligibilityRequirement" type="tns:PromotionEligibilityRequirement" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:complexType name="PromotionBenefits">
			<xs:sequence>
				<xs:element name="Benefit" type="tns:PromotionBenefit" minOccurs="0" maxOccurs="unbounded"/>
			</xs:sequence>
		</xs:complexType>
		<xs:complexType name="PromotionBenefit">
			<xs:sequence>
				<xs:element name="BenefitType" type="xs:string"/>
				<xs:element name="ComponentType" type="xs:string"/>
				<xs:element name="Quantity" type="xs:int" minOccurs="0"/>
				<xs:element name="PercentOff" type="xs:double" minOccurs="0"/>
				<xs:element name="FixedAmount" type="tns:Price" minOccurs="0"/>
				<xs:element name="Ceiling" type="tns:Price" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:complexType name="PromotionEligibilityRequirement">
			<xs:sequence>
				<xs:element name="EligibilityRequirementType" type="xs:string"/>
				<xs:element name="Quantity" type="xs:int" minOccurs="0"/>
				<xs:element name="CurrencyAmount" type="tns:Price" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:complexType name="PromotionItemApplicability">
			<xs:sequence>
				<xs:element name="ASIN" type="xs:string"/>
				<xs:element name="IsInBenefitSet" type="xs:boolean"/>
				<xs:element name="IsInEligibilityRequirementSet" type="xs:boolean"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="VehicleYears">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element ref="tns:VehicleYear" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleYear">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Year" type="xs:nonNegativeInteger" maxOccurs="1"/>
					<xs:element name="IsValid" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleMakes" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleMakes">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleMake" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleMake">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MakeName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="MakeId" type="xs:nonNegativeInteger" maxOccurs="1"/>
					<xs:element name="IsValid" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleModels" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleModels">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleModel" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleModel">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ModelName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="ModelId" type="xs:nonNegativeInteger" maxOccurs="1"/>
					<xs:element name="IsValid" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleTrims" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleTrims">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleTrim" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleTrim">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TrimName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="TrimId" type="xs:nonNegativeInteger" maxOccurs="1"/>
					<xs:element name="IsValid" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleOptions" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleBedOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleBodyStyleOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleBrakesOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleDriveTypeOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleEngineOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleMfrBodyCodeOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleSpringTypesOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleSteeringOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleTransmissionOptions" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:VehicleWheelbaseOptions" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleBedOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleBed" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleBed">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="BedName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="BedId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleBodyStyleOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleBodyStyle" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleBodyStyle">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="BodyStyleName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="BodyStyleId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleBrakesOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleBrakes" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleBrakes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="BrakesName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="BrakesId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleDriveTypeOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleDriveType" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleDriveType">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="DriveTypeName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="DriveTypeId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleEngineOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleEngine" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleEngine">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="EngineName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="EngineId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleMfrBodyCodeOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleMfrBodyCode" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleMfrBodyCode">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="MfrBodyCodeName" type="xs:string" maxOccurs="1"/>
					<xs:element name="MfrBodyCodeId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleSpringTypesOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleSpringTypes" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleSpringTypes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SpringTypesName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="SpringTypesId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleSteeringOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleSteering" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleSteering">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SteeringName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="SteeringId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleTransmissionOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleTransmission" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleTransmission">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TransmissionName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="TransmissionId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleWheelbaseOptions">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:VehicleWheelbase" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleWheelbase">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="WheelbaseName" type="xs:string" minOccurs="0" maxOccurs="1"/>
					<xs:element name="WheelbaseId" type="xs:nonNegativeInteger" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehicleParts">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element name="IsNext" type="xs:boolean" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="IsPrevious" type="xs:boolean" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:Part" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element ref="tns:MissingVehicleAttributes" minOccurs="0" maxOccurs="1"/>
					<xs:element ref="tns:PartBrowseNodeBins" minOccurs="0" />
					<xs:element ref="tns:PartBrandBins" minOccurs="0" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="MissingVehicleAttributes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ParameterName" type="xs:string" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="PartBrowseNodeBins">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Bin" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="PartBrandBins">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Bin" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Part">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Item" minOccurs="0" maxOccurs="1"/>
					<xs:element name="HasPartCompatibility" type="xs:boolean" minOccurs="0" maxOccurs="1" />
					<xs:element ref="tns:VehiclePartFit" minOccurs="0" maxOccurs="1" />
					<xs:element ref="tns:Fitments" minOccurs="0" maxOccurs="1" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="VehiclePartFit">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="IsFit" type="xs:string" maxOccurs="1" />
					<xs:element ref="tns:MissingVehicleAttributes" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Fitments">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TotalFitments" type="xs:nonNegativeInteger" />
					<xs:element name="TotalPages" type="xs:nonNegativeInteger" />
					<xs:element name="FitmentAttributes" type="xs:string" minOccurs="0" />
					<xs:element ref="tns:Fitment" minOccurs="0" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="FitmentAttributes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="FitmentAttribute" type="xs:string" maxOccurs="unbounded" />
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Fitment">
			<xs:complexType>
				<xs:sequence>
				<xs:element name="Year" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Make" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Model" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Trim" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Bed" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="BodyStyle" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Brakes" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="DriveType" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Engine" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="MfrBodyCode" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="SpringTypes" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Steering" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Transmission" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Wheelbase" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Position" type="xs:string" minOccurs="0" maxOccurs="1"/>
				<xs:element name="Notes" type="xs:string" minOccurs="0" maxOccurs="1"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="BrowseNodes">
			<xs:complexType>
				<xs:sequence>
					<xs:element ref="tns:Request" minOccurs="0"/>
					<xs:element ref="tns:BrowseNode" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
	        <xs:element name="Property">
	                <xs:complexType>
	                        <xs:sequence>
	                                <xs:element name="Name" type="xs:string" minOccurs="0"/>
	                                <xs:element name="Value" type="xs:string" minOccurs="0"/>
	                        </xs:sequence>
	                </xs:complexType>
	        </xs:element>
		<xs:element name="BrowseNode">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="BrowseNodeId" type="xs:string" minOccurs="0"/>
					<xs:element name="Name" type="xs:string" minOccurs="0"/>
					<xs:element name="IsCategoryRoot" type="xs:boolean" minOccurs="0"/>
	                                <xs:element name="Properties" minOccurs="0">
	                                        <xs:complexType>
	                                                <xs:sequence>
	                                                        <xs:element ref="tns:Property" maxOccurs="unbounded"/>
	                                                </xs:sequence>
	                                        </xs:complexType>
	                                </xs:element>
					<xs:element name="Children" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element ref="tns:BrowseNode" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="Ancestors" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element ref="tns:BrowseNode" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
			                <xs:element ref="tns:TopSellers" minOccurs="0"/>
	        			<xs:element ref="tns:NewReleases" minOccurs="0"/>
	        			<xs:element ref="tns:TopItemSet" minOccurs="0" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="ListmaniaLists">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ListmaniaList" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="ListId" type="xs:string"/>
								<xs:element name="ListName" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SearchInside">
			<xs:annotation>
				<xs:appinfo>
					<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
						<aws-se:excludeFrom>public</aws-se:excludeFrom>
						<aws-se:excludeFrom>partner</aws-se:excludeFrom>
					</aws-se:restricted>
				</xs:appinfo>
			</xs:annotation>
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TotalExcerpts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="Excerpt" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Checksum" type="xs:string" minOccurs="0"/>
								<xs:element name="PageType" type="xs:string" minOccurs="0"/>
								<xs:element name="PageNumber" type="xs:string" minOccurs="0"/>
								<xs:element name="SequenceNumber" type="xs:string" minOccurs="0"/>
								<xs:element name="Text" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="CartItems">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SubTotal" type="tns:Price" minOccurs="0"/>
					<xs:element name="CartItem" type="tns:CartItem" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SavedForLaterItems">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SubTotal" type="tns:Price" minOccurs="0"/>
					<xs:element name="SavedForLaterItem" type="tns:CartItem" maxOccurs="unbounded"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="CartItem">
			<xs:sequence>
				<xs:element name="CartItemId" type="xs:string"/>
				<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
				<xs:element name="ExchangeId" type="xs:string" minOccurs="0"/>
				<xs:element name="MerchantId" type="xs:string" minOccurs="0"/>
				<xs:element name="SellerId" type="xs:string" minOccurs="0"/>
				<xs:element name="SellerNickname" type="xs:string" minOccurs="0"/>
				<xs:element name="Quantity" type="xs:string"/>
				<xs:element name="Title" type="xs:string" minOccurs="0"/>
				<xs:element name="ProductGroup" type="xs:string" minOccurs="0"/>
				<xs:element name="ListOwner" type="xs:string" minOccurs="0"/>
				<xs:element name="ListType" type="xs:string" minOccurs="0"/>
	                        <xs:element name="MetaData" minOccurs="0">
	                                <xs:complexType>
	                                        <xs:sequence>
	                                                <xs:element name="KeyValuePair" minOccurs="0" maxOccurs="unbounded">
	                                                        <xs:complexType>
	                                                                <xs:sequence>
	                                                                        <xs:element name="Key" type="xs:string"/>
	                                                                        <xs:element name="Value" type="xs:string"/>
	                                                                </xs:sequence>
	                                                        </xs:complexType>
	                                                </xs:element>
	                                        </xs:sequence>
	                                </xs:complexType>
	                        </xs:element>
				<xs:element name="Price" type="tns:Price" minOccurs="0"/>
	                        <xs:element name="ItemTotal" type="tns:Price" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="Transaction">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TransactionId" type="xs:string"/>
					<xs:element name="SellerId" type="xs:string"/>
					<xs:element name="Condition" type="xs:string"/>
					<xs:element name="TransactionDate" type="xs:string"/>
					<xs:element name="TransactionDateEpoch" type="xs:string"/>
					<xs:element name="SellerName" type="xs:string" minOccurs="0"/>
	                                <xs:element name="PayingCustomerId" type="xs:string" minOccurs="0">
	                                    <xs:annotation>
						        <xs:appinfo>
							        <aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
								        <aws-se:excludeFrom>public</aws-se:excludeFrom>
								        <aws-se:excludeFrom>partner</aws-se:excludeFrom>
							        </aws-se:restricted>
						        </xs:appinfo>
					        </xs:annotation>
	                                </xs:element>    
	                                <xs:element name="OrderingCustomerId" type="xs:string" minOccurs="0">
					        <xs:annotation>
						        <xs:appinfo>
							        <aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
								        <aws-se:excludeFrom>public</aws-se:excludeFrom>
								        <aws-se:excludeFrom>partner</aws-se:excludeFrom>
							        </aws-se:restricted>
						        </xs:appinfo>
					        </xs:annotation>
	                                </xs:element>
					<xs:element name="Totals" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Total" type="tns:Price"/>
								<xs:element name="Subtotal" type="tns:Price"/>
								<xs:element name="Tax" type="tns:Price"/>
								<xs:element name="ShippingCharge" type="tns:Price"/>
								<xs:element name="Promotion" type="tns:Price"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="TransactionItems" minOccurs="0">
						<xs:annotation>
							<xs:appinfo>
								<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
									<aws-se:excludeFrom>public</aws-se:excludeFrom>
								</aws-se:restricted>
							</xs:appinfo>
						</xs:annotation>
						<xs:complexType>
							<xs:sequence>
								<xs:element ref="tns:TransactionItem" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="Shipments" minOccurs="0">
						<xs:annotation>
							<xs:appinfo>
								<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
									<aws-se:excludeFrom>public</aws-se:excludeFrom>
								</aws-se:restricted>
							</xs:appinfo>
						</xs:annotation>
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Shipment" maxOccurs="unbounded">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="Condition" type="xs:string"/>
											<xs:element name="DeliveryMethod" type="xs:string"/>
											<xs:element name="ShipmentItems" minOccurs="0">
												<xs:complexType>
													<xs:sequence>
														<xs:element name="TransactionItemId" type="xs:string" maxOccurs="unbounded"/>
													</xs:sequence>
												</xs:complexType>
											</xs:element>
											<xs:element name="Packages" minOccurs="0">
												<xs:complexType>
													<xs:sequence>
														<xs:element name="Package" maxOccurs="unbounded">
															<xs:complexType>
																<xs:sequence>
																	<xs:element name="TrackingNumber" type="xs:string"/>
																	<xs:element name="CarrierName" type="xs:string"/>
																</xs:sequence>
															</xs:complexType>
														</xs:element>
													</xs:sequence>
												</xs:complexType>
											</xs:element>
										</xs:sequence>
									</xs:complexType>
								</xs:element>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="TransactionItem">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="TransactionItemId" type="xs:string"/>
					<xs:element name="Quantity" type="xs:string"/>
					<xs:element name="UnitPrice" type="tns:Price"/>
					<xs:element name="TotalPrice" type="tns:Price"/>
					<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
					<xs:element name="SKU" type="xs:string" minOccurs="0"/>
					<xs:element name="Title" type="xs:string" minOccurs="0"/>
					<xs:element name="ChildTransactionItems" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element ref="tns:TransactionItem" maxOccurs="unbounded"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="Seller">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SellerId" type="xs:string"/>
					<xs:element name="SellerName" type="xs:string" minOccurs="0"/>
				        <xs:element name="SellerLegalName" type="xs:string" minOccurs="0">
	               				<xs:annotation>
	                  				<xs:appinfo>
	                     					<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
	                     						<aws-se:excludeFrom>public</aws-se:excludeFrom>
	                     					</aws-se:restricted>
	                  				</xs:appinfo>
	               				</xs:annotation>
	            			</xs:element>		
	            			<xs:element name="Nickname" type="xs:string" minOccurs="0"/>
					<xs:element name="GlancePage" type="xs:string" minOccurs="0"/>
					<xs:element name="About" type="xs:string" minOccurs="0"/>
					<xs:element name="MoreAbout" type="xs:string" minOccurs="0"/>
					<xs:element name="Location" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="UserDefinedLocation" type="xs:string" minOccurs="0"/>
								<xs:element name="City" type="xs:string" minOccurs="0"/>
								<xs:element name="State" type="xs:string" minOccurs="0"/>
								<xs:element name="Country" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="AverageFeedbackRating" type="xs:decimal" minOccurs="0"/>
					<xs:element name="TotalFeedback" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalFeedbackPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="SellerFeedbackSummary" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="FeedbackDateRange" minOccurs="0" maxOccurs="unbounded">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="SellerFeedbackRating" minOccurs="0" maxOccurs="unbounded">
												<xs:complexType>
													<xs:sequence>
														<xs:element name="Count" type="xs:nonNegativeInteger" minOccurs="0"/>
														<xs:element name="Percentage" type="xs:nonNegativeInteger" minOccurs="0"/>
													</xs:sequence>
												<xs:attribute name="Type" type="xs:string"/>
												</xs:complexType>
											</xs:element>
										</xs:sequence>
										<xs:attribute name="Period" type="xs:string"/>
									</xs:complexType>
								</xs:element>     	
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element ref="tns:SellerFeedback" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="SellerFeedback">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Feedback" maxOccurs="unbounded">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Rating" type="xs:nonNegativeInteger" minOccurs="0"/>
								<xs:element name="Comment" type="xs:string" minOccurs="0"/>
								<xs:element name="Date" type="xs:string" minOccurs="0"/>
								<xs:element name="RatedBy" type="xs:string" minOccurs="0"/>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="Address">
			<xs:sequence>
				<xs:element name="Name" type="xs:string" minOccurs="0"/>
				<xs:element name="Address1" type="xs:string" minOccurs="0"/>
				<xs:element name="Address2" type="xs:string" minOccurs="0"/>
				<xs:element name="Address3" type="xs:string" minOccurs="0"/>
				<xs:element name="City" type="xs:string" minOccurs="0"/>
				<xs:element name="State" type="xs:string" minOccurs="0"/>
				<xs:element name="PostalCode" type="xs:string" minOccurs="0"/>
				<xs:element name="Country" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="SellerListing">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="ExchangeId" type="xs:string" minOccurs="0"/>
					<xs:element name="ListingId" type="xs:string" minOccurs="0"/>
					<xs:element name="ASIN" type="xs:string" minOccurs="0"/>
	                                <xs:element name="SKU" type="xs:string" minOccurs="0"/>
	                                <xs:element name="UPC" type="xs:string" minOccurs="0"/>
	                                <xs:element name="EAN" type="xs:string" minOccurs="0"/>
	                                <xs:element name="WillShipExpedited" type="xs:boolean" minOccurs="0"/>
	                                <xs:element name="WillShipInternational" type="xs:boolean" minOccurs="0"/>
					<xs:element name="Title" type="xs:string" minOccurs="0"/>
					<xs:element name="Price" type="tns:Price" minOccurs="0"/>
					<xs:element name="StartDate" type="xs:string" minOccurs="0"/>
					<xs:element name="EndDate" type="xs:string" minOccurs="0"/>
					<xs:element name="Status" type="xs:string" minOccurs="0"/>
					<xs:element name="Quantity" type="xs:string" minOccurs="0"/>
					<xs:element name="Condition" type="xs:string" minOccurs="0"/>
					<xs:element name="SubCondition" type="xs:string" minOccurs="0"/>
					<xs:element ref="tns:Seller" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="Price">
			<xs:sequence>
				<xs:element name="Amount" type="xs:integer" minOccurs="0"/>
				<xs:element name="CurrencyCode" type="xs:string" minOccurs="0"/>
				<xs:element name="FormattedPrice" type="xs:string"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="ImageSet">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="SwatchImage" type="tns:Image" minOccurs="0"/>
					<xs:element name="SmallImage" type="tns:Image" minOccurs="0"/>
	                                <xs:element name="ThumbnailImage" type="tns:Image" minOccurs="0"/>
	                                <xs:element name="TinyImage" type="tns:Image" minOccurs="0"/>
					<xs:element name="MediumImage" type="tns:Image" minOccurs="0"/>
					<xs:element name="LargeImage" type="tns:Image" minOccurs="0"/>
				</xs:sequence>
				<xs:attribute name="Category" type="xs:string"/>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="Image">
			<xs:sequence>
				<xs:element name="URL" type="xs:string"/>
				<xs:element name="Height" type="tns:DecimalWithUnits"/>
				<xs:element name="Width" type="tns:DecimalWithUnits"/>
				<xs:element name="IsVerified" type="xs:string" minOccurs="0"/>
			</xs:sequence>
		</xs:complexType>
		<xs:element name="ItemAttributes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Actor" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Address" type="tns:Address" minOccurs="0"/>
					<xs:element name="Age" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="AmazonMaximumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="AmazonMinimumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="AnalogVideoFormat" type="xs:string" minOccurs="0"/>
					<xs:element name="ApertureModes" type="xs:string" minOccurs="0"/>
					<xs:element name="Artist" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="AspectRatio" type="xs:string" minOccurs="0"/>
					<xs:element name="AssemblyInstructions" type="xs:string" minOccurs="0"/>
					<xs:element name="AssemblyRequired" type="xs:string" minOccurs="0"/>
					<xs:element name="AudienceRating" type="xs:string" minOccurs="0"/>
					<xs:element name="AudioFormat" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Author" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="BackFinding" type="xs:string" minOccurs="0"/>
					<xs:element name="BandMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="BatteriesIncluded" type="xs:string" minOccurs="0"/>
					<xs:element name="BatteriesRequired" type="xs:string" minOccurs="0"/>
	                                <xs:element name="Batteries" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="BatteryDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="BatteryType" type="xs:string" minOccurs="0"/>
					<xs:element name="BezelMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="Binding" type="xs:string" minOccurs="0"/>
					<xs:element name="Brand" type="xs:string" minOccurs="0"/>
					<xs:element name="CalendarType" type="xs:string" minOccurs="0"/>
					<xs:element name="CameraManualFeatures" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="CaseDiameter" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="CaseMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="CaseThickness" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="CaseType" type="xs:string" minOccurs="0"/>
					<xs:element name="CatalogNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="Category" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="CategoryBin" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="CDRWDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="ChainType" type="xs:string" minOccurs="0"/>
					<xs:element name="Character" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="CEROAgeRating" type="xs:string" minOccurs="0"/>
					<xs:element name="ClaspType" type="xs:string" minOccurs="0"/>
					<xs:element name="ClothingSize" type="xs:string" minOccurs="0"/>
					<xs:element name="ClubType" type="xs:string" minOccurs="0"/>
					<xs:element name="Color" type="xs:string" minOccurs="0"/>
					<xs:element name="Compatibility" type="xs:string" minOccurs="0"/>
					<xs:element name="CompatibleDevices" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="ComputerHardwareType" type="xs:string" minOccurs="0"/>
					<xs:element name="ComputerPlatform" type="xs:string" minOccurs="0"/>
					<xs:element name="Connectivity" type="xs:string" minOccurs="0"/>
					<xs:element name="ContinuousShootingSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Country" type="xs:string" minOccurs="0"/>
					<xs:element name="CPUManufacturer" type="xs:string" minOccurs="0"/>
					<xs:element name="CPUSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="CPUType" type="xs:string" minOccurs="0"/>
					<xs:element name="Creator" minOccurs="0" maxOccurs="unbounded">
						<xs:complexType>
							<xs:simpleContent>
								<xs:extension base="xs:string">
									<xs:attribute name="Role" type="xs:string" use="required"/>
								</xs:extension>
							</xs:simpleContent>
						</xs:complexType>
					</xs:element>
					<xs:element name="Cuisine" type="xs:string" minOccurs="0"/>
					<xs:element name="DataLinkProtocol" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="DeliveryOption" type="xs:string" minOccurs="0"/>
					<xs:element name="DelayBetweenShots" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Department" type="xs:string" minOccurs="0"/>
					<xs:element name="DeweyDecimalNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="DialColor" type="xs:string" minOccurs="0"/>
					<xs:element name="DialWindowMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="DigitalZoom" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Director" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="DisplayColorSupport" type="xs:string" minOccurs="0"/>
					<xs:element name="DisplaySize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="DrumSetPieceQuantity" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DVDLayers" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DVDRWDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="DVDSides" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DPCI" type="xs:string" minOccurs="0"/>
					<xs:element name="EAN" type="xs:string" minOccurs="0"/>
					<xs:element name="Edition" type="xs:string" minOccurs="0"/>
					<xs:element name="EducationalFocus" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="EpisodeSequence" type="xs:string" minOccurs="0"/>
					<xs:element name="Ethnicity" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="ESRBAgeRating" type="xs:string" minOccurs="0"/>
					<xs:element name="ExternalDisplaySupportDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="FabricType" type="xs:string" minOccurs="0"/>
					<xs:element name="FaxNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="Feature" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="FilmColorType" type="xs:string" minOccurs="0"/>
					<xs:element name="FirstIssueLeadTime" type="tns:StringWithUnits" minOccurs="0"/>
	                                <xs:element name="FlavorName" type="xs:string" minOccurs="0"/>
					<xs:element name="FloppyDiskDriveDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="Format" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="FormFactor" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="GemType" type="xs:string" minOccurs="0"/>
					<xs:element name="GemTypeSetElement" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Gender" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Genre" type="xs:string" minOccurs="0"/>
					<xs:element name="GLProductGroup" type="xs:string" minOccurs="0"/>
	                                <xs:element name="GolfClubFlex" type="xs:string" minOccurs="0"/>
	                                <xs:element name="GolfClubLoft" type="xs:string" minOccurs="0"/>
					<xs:element name="GraphicsCardInterface" type="xs:string" minOccurs="0"/>
					<xs:element name="GraphicsDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="GraphicsMemorySize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="GuitarAttribute" type="xs:string" minOccurs="0"/>
					<xs:element name="GuitarBridgeSystem" type="xs:string" minOccurs="0"/>
					<xs:element name="GuitarPickThickness" type="xs:string" minOccurs="0"/>
					<xs:element name="GuitarPickupConfiguration" type="xs:string" minOccurs="0"/>
					<xs:element name="HandOrientation" type="xs:string" minOccurs="0"/>
					<xs:element name="HardDiskCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="HardDiskSize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="HardDiskInterface" type="xs:string" minOccurs="0"/>
					<xs:element name="HardwarePlatform" type="xs:string" minOccurs="0"/>
					<xs:element name="HasAutoFocus" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasBurstMode" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasInCameraEditing" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasRedEyeReduction" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasSelfTimer" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasTripodMount" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasVideoOut" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasViewfinder" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HazardousMaterialType" type="xs:string" minOccurs="0"/>
	            <xs:element name="HoursOfOperation" type="xs:string" minOccurs="0"/>
					<xs:element name="IncludedSoftware" type="xs:string" minOccurs="0"/>
					<xs:element name="IncludesMp3Player" type="xs:boolean" minOccurs="0"/>
					<xs:element name="Ingredients" type="xs:string" minOccurs="0"/>
	                <xs:element name="IngredientsSetElement" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="InstrumentKey" type="xs:string" minOccurs="0"/>
					<xs:element name="Interest" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
	                                <xs:element name="IsAdultProduct" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsAutographed" type="xs:boolean" minOccurs="0"/>
					<xs:element name="ISBN" type="xs:string" minOccurs="0"/>
					<xs:element name="IsEligibleForTradeIn" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsFragile" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsLabCreated" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsMemorabilia" type="xs:boolean" minOccurs="0"/>
					<xs:element name="ISOEquivalent" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="IsPreannounce" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IssuesPerYear" type="xs:string" minOccurs="0"/>
					<xs:element name="ItemDimensions" minOccurs="0" maxOccurs="1">
							<xs:complexType>
	       							<xs:sequence>
	       								<xs:element name="Height" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Length" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Weight" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Width" type="tns:DecimalWithUnits" minOccurs="0"/>
	       							</xs:sequence>
	       						</xs:complexType>
	       					</xs:element>
					<xs:element name="KeyboardDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="Label" type="xs:string" minOccurs="0"/>
					<xs:element name="LanguageName" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Languages" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Language" minOccurs="0" maxOccurs="unbounded">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="Name" type="xs:string"/>
											<xs:element name="Type" type="xs:string" minOccurs="0"/>
											<xs:element name="AudioFormat" type="xs:string" minOccurs="0"/>
										</xs:sequence>
									</xs:complexType>
								</xs:element>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="LegalDisclaimer" type="xs:string" minOccurs="0"/>
					<xs:element name="LensType" type="xs:string" minOccurs="0"/>
					<xs:element name="LineVoltage" type="xs:string" minOccurs="0"/>
					<xs:element name="ListPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="LongSynopsis" type="xs:string" minOccurs="0"/>
					<xs:element name="MacroFocusRange" type="xs:string" minOccurs="0"/>
					<xs:element name="MagazineType" type="xs:string" minOccurs="0"/>
					<xs:element name="MalletHardness" type="xs:string" minOccurs="0"/>
					<xs:element name="Manufacturer" type="xs:string" minOccurs="0"/>
					<xs:element name="ManufacturerLaborWarrantyDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="ManufacturerMaximumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="ManufacturerMinimumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="ManufacturerPartsWarrantyDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="MaterialTypeSetElement" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="MaximumAperture" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumColorDepth" type="xs:string" minOccurs="0"/>
					<xs:element name="MaximumFocalLength" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumHighResolutionImages" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="MaximumHorizontalResolution" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="MaximumLowResolutionImages" type="xs:string" minOccurs="0"/>
					<xs:element name="MaximumResolution" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumShutterSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumVerticalResolution" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="MaximumWeightRecommendation" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MediaType" type="xs:string" minOccurs="0"/>
					<xs:element name="MemorySlotsAvailable" type="xs:string" minOccurs="0"/>
					<xs:element name="MetalStamp" type="xs:string" minOccurs="0"/>
					<xs:element name="MetalType" type="xs:string" minOccurs="0"/>
					<xs:element name="MiniMovieDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MinimumFocalLength" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MinimumShutterSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Model" type="xs:string" minOccurs="0"/>
					<xs:element name="ModelYear" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="ModemDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MonitorSize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MonitorViewableDiagonalSize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MouseDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MPN" type="xs:string" minOccurs="0"/>
					<xs:element name="MusicalStyle" type="xs:string" minOccurs="0"/>
					<xs:element name="NativeResolution" type="xs:string" minOccurs="0"/>
					<xs:element name="Neighborhood" type="xs:string" minOccurs="0"/>
					<xs:element name="NetworkInterfaceDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="NotebookDisplayTechnology" type="xs:string" minOccurs="0"/>
					<xs:element name="NotebookPointingDeviceDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="NumberOfDiscs" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfIssues" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfItems" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfKeys" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfPearls" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfRapidFireShots" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfStones" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfStrings" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfTracks" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="OperatingSystem" type="xs:string" minOccurs="0"/>
					<xs:element name="OpticalSensorResolution" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="OpticalZoom" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="OriginalReleaseDate" type="xs:string" minOccurs="0"/>
					<xs:element name="OriginalAirDate" type="xs:string" minOccurs="0"/>
					<xs:element name="OutputWattage" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="PackageDimensions" minOccurs="0" maxOccurs="1">
							<xs:complexType>
	       							<xs:sequence>
	       								<xs:element name="Height" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Length" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Weight" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Width" type="tns:DecimalWithUnits" minOccurs="0"/>
	       							</xs:sequence>
	       						</xs:complexType>
	       				</xs:element>
					<xs:element name="PackageQuantity" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="PantLength" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="PantSize" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="PearlLustre" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlMinimumColor" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlShape" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlStringingMethod" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlSurfaceBlemishes" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlType" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlUniformity" type="xs:string" minOccurs="0"/>
					<xs:element name="PhoneNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="PhotoFlashType" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="PictureFormat" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Platform" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="PriceRating" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="PrimaryColor" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="ProcessorCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="ProductGroup" type="xs:string" minOccurs="0"/>
	                                <xs:element name="ProductSiteLaunchDate" type="xs:string" minOccurs="0"/>
	       				<xs:element name="ProductTypeName" type="xs:string" minOccurs="0"/>
					<xs:element name="ProductTypeSubcategory" type="xs:string" minOccurs="0"/>
					<xs:element name="PromotionalTag" type="xs:string" minOccurs="0">
						<xs:annotation>
							<xs:appinfo>
								<aws-se:restricted xmlns:aws-se="http://webservices.amazon.com/AWS-SchemaExtensions">
									<aws-se:excludeFrom>public</aws-se:excludeFrom>
									<aws-se:excludeFrom>partner</aws-se:excludeFrom>
								</aws-se:restricted>
							</xs:appinfo>
						</xs:annotation>
					</xs:element>
					<xs:element name="PublicationDate" type="xs:string" minOccurs="0"/>
					<xs:element name="Publisher" type="xs:string" minOccurs="0"/>
					<xs:element name="POBoxShippingExcluded" type="xs:string" minOccurs="0"/>
					<xs:element name="ReadingLevel" type="xs:string" minOccurs="0"/>
					<xs:element name="ReturnMethod" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="RecorderTrackCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="RegionCode" type="xs:string" minOccurs="0"/>
					<xs:element name="RegionOfOrigin" type="xs:string" minOccurs="0"/>
					<xs:element name="ReturnPolicy" type="xs:string" minOccurs="0"/>
					<xs:element name="ReleaseDate" type="xs:string" minOccurs="0"/>
					<xs:element name="RemovableMemory" type="xs:string" minOccurs="0"/>
					<xs:element name="RemovableStorage" type="xs:string" minOccurs="0"/>
					<xs:element name="RequiredVoltageRange" type="xs:string" minOccurs="0"/>
					<xs:element name="ResolutionModes" type="xs:string" minOccurs="0"/>
					<xs:element name="RingSize" type="xs:string" minOccurs="0"/>
					<xs:element name="RunningTime" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="ScentName" type="xs:string" minOccurs="0"/>
					<xs:element name="SeasonSequence" type="xs:string" minOccurs="0"/>
					<xs:element name="SecondaryCacheSize" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="SettingType" type="xs:string" minOccurs="0"/>
					<xs:element name="ShaftMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="ShoeSize" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="ShortSynopsis" type="xs:string" minOccurs="0"/>
					<xs:element name="Size" type="xs:string" minOccurs="0"/>
					<xs:element name="SizePerPearl" type="xs:string" minOccurs="0"/>
					<xs:element name="SkillLevel" type="xs:string" minOccurs="0"/>
					<xs:element name="SKU" type="xs:string" minOccurs="0"/>
					<xs:element name="SoldInStores" type="xs:string" minOccurs="0"/>
					<xs:element name="SoundCardDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="SpeakerCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="SpeakerDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="SpecialFeatures" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="StartYear" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneClarity" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneColor" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneCut" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneShape" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Studio" type="xs:string" minOccurs="0"/>
					<xs:element name="Style" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionLength" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="SupportedImageType" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="SupportedMediaSize" type="xs:string" minOccurs="0"/>
					<xs:element name="SystemBusSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="SystemMemorySizeMax" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="SystemMemorySize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="SystemMemoryType" type="xs:string" minOccurs="0"/>
					<xs:element name="TargetBrand" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="TellingPageIndicator" type="xs:string" minOccurs="0"/>
					<xs:element name="TheatricalReleaseDate" type="xs:string" minOccurs="0"/>
					<xs:element name="Title" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalDiamondWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="TotalExternalBaysFree" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalFirewirePorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalGemWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="TotalInternalBaysFree" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalMetalWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="TotalNTSCPALPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalParallelPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPCCardSlots" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPCISlotsFree" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalSerialPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalSVideoOutPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalUSB2Ports" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalUSBPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalVGAOutPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TrackSequence" type="xs:string" minOccurs="0"/>
					<xs:element name="TradeInValue" type="tns:Price" minOccurs="0"/>
					<xs:element name="UPC" type="xs:string" minOccurs="0"/>
					<xs:element name="VariationDenomination" type="xs:string" minOccurs="0"/>
					<xs:element name="VariationDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="Warranty" type="xs:string" minOccurs="0"/>
					<xs:element name="WatchMovementType" type="xs:string" minOccurs="0"/>
					<xs:element name="WaterResistanceDepth" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="WEEETaxValue" type="tns:Price" minOccurs="0"/>
					<xs:element name="WirelessMicrophoneFrequency" type="xs:nonNegativeInteger" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:element name="MerchantItemAttributes">
			<xs:complexType>
				<xs:sequence>
					<xs:element name="Actor" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Address" type="tns:Address" minOccurs="0"/>
					<xs:element name="AmazonMaximumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="AmazonMinimumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="ApertureModes" type="xs:string" minOccurs="0"/>
					<xs:element name="Artist" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="AspectRatio" type="xs:string" minOccurs="0"/>
					<xs:element name="AssemblyInstructions" type="xs:string" minOccurs="0"/>
					<xs:element name="AssemblyRequired" type="xs:string" minOccurs="0"/>
					<xs:element name="AudienceRating" type="xs:string" minOccurs="0"/>
					<xs:element name="AudioFormat" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Author" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="BackFinding" type="xs:string" minOccurs="0"/>
					<xs:element name="BandMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="BatteriesIncluded" type="xs:string" minOccurs="0"/>
					<xs:element name="BatteriesRequired" type="xs:string" minOccurs="0"/>
	                                <xs:element name="Batteries" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="BatteryDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="BatteryType" type="xs:string" minOccurs="0"/>
					<xs:element name="BezelMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="Binding" type="xs:string" minOccurs="0"/>
					<xs:element name="Brand" type="xs:string" minOccurs="0"/>
					<xs:element name="CalendarType" type="xs:string" minOccurs="0"/>
					<xs:element name="CameraManualFeatures" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="CaseDiameter" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="CaseMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="CaseThickness" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="CaseType" type="xs:string" minOccurs="0"/>
					<xs:element name="CatalogNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="CDRWDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="ChainType" type="xs:string" minOccurs="0"/>
					<xs:element name="ClaspType" type="xs:string" minOccurs="0"/>
					<xs:element name="ClothingSize" type="xs:string" minOccurs="0"/>
					<xs:element name="Color" type="xs:string" minOccurs="0"/>
					<xs:element name="Compatibility" type="xs:string" minOccurs="0"/>
					<xs:element name="ComputerHardwareType" type="xs:string" minOccurs="0"/>
					<xs:element name="ComputerPlatform" type="xs:string" minOccurs="0"/>
					<xs:element name="Connectivity" type="xs:string" minOccurs="0"/>
					<xs:element name="ContinuousShootingSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Country" type="xs:string" minOccurs="0"/>
					<xs:element name="CountryOfOrigin" type="xs:string" minOccurs="0"/>
					<xs:element name="CPUManufacturer" type="xs:string" minOccurs="0"/>
					<xs:element name="CPUSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="CPUType" type="xs:string" minOccurs="0"/>
					<xs:element name="Creator" minOccurs="0" maxOccurs="unbounded">
						<xs:complexType>
							<xs:simpleContent>
								<xs:extension base="xs:string">
									<xs:attribute name="Role" type="xs:string" use="required"/>
								</xs:extension>
							</xs:simpleContent>
						</xs:complexType>
					</xs:element>
					<xs:element name="Cuisine" type="xs:string" minOccurs="0"/>
					<xs:element name="Customizable" type="xs:string" minOccurs="0"/>
					<xs:element name="DelayBetweenShots" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="DeliveryOption" type="xs:string" minOccurs="0"/>
					<xs:element name="Department" type="xs:string" minOccurs="0"/>
					<xs:element name="Description" type="xs:string" minOccurs="0"/>
					<xs:element name="DeweyDecimalNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="DialColor" type="xs:string" minOccurs="0"/>
					<xs:element name="DialWindowMaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="DigitalZoom" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Director" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="DisplaySize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="DrumSetPieceQuantity" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DVDLayers" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DVDRWDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="DVDSides" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="DPCI" type="xs:string" minOccurs="0"/>
					<xs:element name="EAN" type="xs:string" minOccurs="0"/>
					<xs:element name="Edition" type="xs:string" minOccurs="0"/>
					<xs:element name="ESRBAgeRating" type="xs:string" minOccurs="0"/>
					<xs:element name="ExternalDisplaySupportDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="FabricType" type="xs:string" minOccurs="0"/>
					<xs:element name="FaxNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="Feature" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="FirstIssueLeadTime" type="tns:StringWithUnits" minOccurs="0"/>
					<xs:element name="FloppyDiskDriveDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="Format" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="FixedShippingCharge" type="tns:Price" minOccurs="0"/>
					<xs:element name="GemType" type="xs:string" minOccurs="0"/>
					<xs:element name="GraphicsCardInterface" type="xs:string" minOccurs="0"/>
					<xs:element name="GraphicsDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="GraphicsMemorySize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="GuitarAttribute" type="xs:string" minOccurs="0"/>
					<xs:element name="GuitarBridgeSystem" type="xs:string" minOccurs="0"/>
					<xs:element name="GuitarPickThickness" type="xs:string" minOccurs="0"/>
					<xs:element name="GuitarPickupConfiguration" type="xs:string" minOccurs="0"/>
					<xs:element name="HardDiskCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="HardDiskSize" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="HasAutoFocus" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasBurstMode" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasInCameraEditing" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasRedEyeReduction" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasSelfTimer" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasTripodMount" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasVideoOut" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HasViewfinder" type="xs:boolean" minOccurs="0"/>
					<xs:element name="HazardousMaterialType" type="xs:string" minOccurs="0"/>
			                <xs:element name="HoursOfOperation" type="xs:string" minOccurs="0"/>
					<xs:element name="IncludedSoftware" type="xs:string" minOccurs="0"/>
					<xs:element name="IncludesMp3Player" type="xs:boolean" minOccurs="0"/>
					<xs:element name="Indications" type="xs:string" minOccurs="0"/>
					<xs:element name="Ingredients" type="xs:string" minOccurs="0"/>
					<xs:element name="IngredientsSetElement" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="InstrumentKey" type="xs:string" minOccurs="0"/>
					<xs:element name="IsAutographed" type="xs:boolean" minOccurs="0"/>
					<xs:element name="ISBN" type="xs:string" minOccurs="0"/>
					<xs:element name="IsEmailNotifyAvailable" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsFragile" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsLabCreated" type="xs:boolean" minOccurs="0"/>
					<xs:element name="IsMemorabilia" type="xs:boolean" minOccurs="0"/>
					<xs:element name="ISOEquivalent" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="IssuesPerYear" type="xs:string" minOccurs="0"/>
					<xs:element name="ItemDimensions" minOccurs="0" maxOccurs="1">
							<xs:complexType>
	       							<xs:sequence>
	       								<xs:element name="Height" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Length" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Weight" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Width" type="tns:DecimalWithUnits" minOccurs="0"/>
	       							</xs:sequence>
	       						</xs:complexType>
	       					</xs:element>
					<xs:element name="KeyboardDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="Label" type="xs:string" minOccurs="0"/>
					<xs:element name="Languages" minOccurs="0">
						<xs:complexType>
							<xs:sequence>
								<xs:element name="Language" minOccurs="0" maxOccurs="unbounded">
									<xs:complexType>
										<xs:sequence>
											<xs:element name="Name" type="xs:string"/>
											<xs:element name="Type" type="xs:string"/>
											<xs:element name="AudioFormat" type="xs:string" minOccurs="0"/>
										</xs:sequence>
									</xs:complexType>
								</xs:element>
							</xs:sequence>
						</xs:complexType>
					</xs:element>
					<xs:element name="LegalDisclaimer" type="xs:string" minOccurs="0"/>
					<xs:element name="LineVoltage" type="xs:string" minOccurs="0"/>
					<xs:element name="ListPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="MacroFocusRange" type="xs:string" minOccurs="0"/>
					<xs:element name="MagazineType" type="xs:string" minOccurs="0"/>
					<xs:element name="MalletHardness" type="xs:string" minOccurs="0"/>
					<xs:element name="Manufacturer" type="xs:string" minOccurs="0"/>
					<xs:element name="ManufacturerLaborWarrantyDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="ManufacturerMaximumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="ManufacturerMinimumAge" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="ManufacturerPartsWarrantyDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MaterialType" type="xs:string" minOccurs="0"/>
					<xs:element name="MaximumAperture" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumColorDepth" type="xs:string" minOccurs="0"/>
					<xs:element name="MaximumFocalLength" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumHighResolutionImages" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="MaximumHorizontalResolution" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="MaximumLowResolutionImages" type="xs:string" minOccurs="0"/>
					<xs:element name="MaximumResolution" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumShutterSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MaximumVerticalResolution" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="MaximumWeightRecommendation" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MemorySlotsAvailable" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="MetalStamp" type="xs:string" minOccurs="0"/>
					<xs:element name="MetalType" type="xs:string" minOccurs="0"/>
					<xs:element name="MiniMovieDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MinimumAdvertisedPrice" type="tns:Price" minOccurs="0"/>
					<xs:element name="MinimumFocalLength" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MinimumShutterSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Model" type="xs:string" minOccurs="0"/>
					<xs:element name="ModelYear" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="ModemDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MonitorSize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MonitorViewableDiagonalSize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="MouseDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="MPN" type="xs:string" minOccurs="0"/>
					<xs:element name="MusicalStyle" type="xs:string" minOccurs="0"/>
					<xs:element name="NativeResolution" type="xs:string" minOccurs="0"/>
					<xs:element name="Neighborhood" type="xs:string" minOccurs="0"/>
					<xs:element name="NetworkInterfaceDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="NotebookDisplayTechnology" type="xs:string" minOccurs="0"/>
					<xs:element name="NotebookPointingDeviceDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="NumberOfDiscs" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfIssues" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfItems" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfKeys" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfPages" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfPearls" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfRapidFireShots" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfStones" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfStrings" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="NumberOfTracks" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="OpticalZoom" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="OriginalReleaseDate" type="xs:string" minOccurs="0"/>
					<xs:element name="OutputWattage" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="PackageDimensions" minOccurs="0" maxOccurs="1">
							<xs:complexType>
	       							<xs:sequence>
	       								<xs:element name="Height" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Length" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Weight" type="tns:DecimalWithUnits" minOccurs="0"/>
	       								<xs:element name="Width" type="tns:DecimalWithUnits" minOccurs="0"/>
	       							</xs:sequence>
	       						</xs:complexType>
	       				</xs:element>
					<xs:element name="PearlLustre" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlMinimumColor" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlShape" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlStringingMethod" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlSurfaceBlemishes" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlType" type="xs:string" minOccurs="0"/>
					<xs:element name="PearlUniformity" type="xs:string" minOccurs="0"/>
					<xs:element name="PhoneNumber" type="xs:string" minOccurs="0"/>
					<xs:element name="PhotoFlashType" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="PictureFormat" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="Platform" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="PriceRating" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="ProcessorCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="ProductGroup" type="xs:string" minOccurs="0"/>
					<xs:element name="PromotionalTag" type="xs:string" minOccurs="0"/>
					<xs:element name="POBoxShippingExcluded" type="xs:string" minOccurs="0"/>
					<xs:element name="PublicationDate" type="xs:string" minOccurs="0"/>
					<xs:element name="Publisher" type="xs:string" minOccurs="0"/>
					<xs:element name="PurchasingChannel" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="ReadingLevel" type="xs:string" minOccurs="0"/>
					<xs:element name="RecorderTrackCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="RegionCode" type="xs:string" minOccurs="0"/>
					<xs:element name="RegionOfOrigin" type="xs:string" minOccurs="0"/>
					<xs:element name="ReleaseDate" type="xs:string" minOccurs="0"/>
					<xs:element name="ReturnMethod" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="RemovableMemory" type="xs:string" minOccurs="0"/>
					<xs:element name="ResolutionModes" type="xs:string" minOccurs="0"/>
					<xs:element name="ReturnPolicy" type="xs:string" minOccurs="0"/>
					<xs:element name="RingSize" type="xs:string" minOccurs="0"/>
					<xs:element name="SafetyWarning" type="xs:string" minOccurs="0"/>
					<xs:element name="SalesRestriction" type="xs:string" minOccurs="0"/>
					<xs:element name="SecondaryCacheSize" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="SettingType" type="xs:string" minOccurs="0"/>
					<xs:element name="Size" type="xs:string" minOccurs="0"/>
					<xs:element name="SKU" type="xs:string" minOccurs="0"/>
					<xs:element name="SoldInStores" type="xs:string" minOccurs="0"/>
					<xs:element name="SizePerPearl" type="xs:string" minOccurs="0"/>
					<xs:element name="SkillLevel" type="xs:string" minOccurs="0"/>
					<xs:element name="SoundCardDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="SpeakerCount" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="SpeakerDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="SpecialFeatures" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="StoneClarity" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneColor" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneCut" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneShape" type="xs:string" minOccurs="0"/>
					<xs:element name="StoneWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="Studio" type="xs:string" minOccurs="0"/>
					<xs:element name="SubscriptionLength" type="tns:NonNegativeIntegerWithUnits" minOccurs="0"/>
					<xs:element name="SupportedImageType" type="xs:string" minOccurs="0" maxOccurs="unbounded"/>
					<xs:element name="SystemBusSpeed" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="SystemMemorySizeMax" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="SystemMemorySize" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="SystemMemoryType" type="xs:string" minOccurs="0"/>
					<xs:element name="TellingPageIndicator" type="xs:string" minOccurs="0"/>
					<xs:element name="TheatricalReleaseDate" type="xs:string" minOccurs="0"/>
					<xs:element name="Title" type="xs:string" minOccurs="0"/>
					<xs:element name="TotalDiamondWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="TotalExternalBaysFree" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalFirewirePorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalGemWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="TotalInternalBaysFree" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalMetalWeight" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="TotalNTSCPALPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalParallelPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPCCardSlots" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalPCISlotsFree" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalSerialPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalSVideoOutPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalUSB2Ports" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalUSBPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="TotalVGAOutPorts" type="xs:nonNegativeInteger" minOccurs="0"/>
					<xs:element name="UPC" type="xs:string" minOccurs="0"/>
					<xs:element name="VariationDenomination" type="xs:string" minOccurs="0"/>
					<xs:element name="VariationDescription" type="xs:string" minOccurs="0"/>
					<xs:element name="VendorRebate" minOccurs="0">
	                	<xs:complexType>
	                    	<xs:sequence>
	                        	<xs:element name="Type" type="xs:string" minOccurs="0"/>
	                            <xs:element name="StartDate" type="xs:string" minOccurs="0"/>
	                            <xs:element name="EndDate" type="xs:string" minOccurs="0"/>
	                        </xs:sequence>
	                    </xs:complexType>
	                </xs:element>
					<xs:element name="Warranty" type="xs:string" minOccurs="0"/>
					<xs:element name="WatchMovementType" type="xs:string" minOccurs="0"/>
					<xs:element name="WebsiteBuyability" type="xs:string" minOccurs="0"/>
					<xs:element name="WaterResistanceDepth" type="tns:DecimalWithUnits" minOccurs="0"/>
					<xs:element name="WirelessMicrophoneFrequency" type="xs:nonNegativeInteger" minOccurs="0"/>
				</xs:sequence>
			</xs:complexType>
		</xs:element>
		<xs:complexType name="NonNegativeIntegerWithUnits">
			<xs:simpleContent>
				<xs:extension base="xs:nonNegativeInteger">
					<xs:attribute name="Units" type="xs:string" use="required"/>
				</xs:extension>
			</xs:simpleContent>
		</xs:complexType>
		<xs:complexType name="DecimalWithUnits">
			<xs:simpleContent>
				<xs:extension base="xs:decimal">
					<xs:attribute name="Units" type="xs:string" use="required"/>
				</xs:extension>
			</xs:simpleContent>
		</xs:complexType>
		<xs:complexType name="StringWithUnits">
			<xs:simpleContent>
				<xs:extension base="xs:string">
					<xs:attribute name="Units" type="xs:string" use="required"/>
				</xs:extension>
			</xs:simpleContent>
		</xs:complexType>
	        <xs:simpleType name="positiveIntegerOrAll">
	                <xs:union>
	                        <xs:simpleType>
	                                <xs:restriction base="xs:positiveInteger"/>
	                        </xs:simpleType>
	                        <xs:simpleType>
	                                <xs:restriction base="xs:string">
	                                <xs:enumeration value="All"/>
	                                </xs:restriction>
	                        </xs:simpleType>
	                </xs:union>
	       </xs:simpleType>
	</xs:schema>
    </types>

    <message name="HelpRequestMsg">
	<part name="body" element="tns:Help"/>
    </message>
    <message name="HelpResponseMsg">
	<part name="body" element="tns:HelpResponse"/>
    </message>
    <message name="ItemSearchRequestMsg">
	<part name="body" element="tns:ItemSearch"/>
    </message>
    <message name="ItemSearchResponseMsg">
	<part name="body" element="tns:ItemSearchResponse"/>
    </message>
    <message name="ItemLookupRequestMsg">
	<part name="body" element="tns:ItemLookup"/>
    </message>
    <message name="ItemLookupResponseMsg">
	<part name="body" element="tns:ItemLookupResponse"/>
    </message>
    <message name="BrowseNodeLookupRequestMsg">
	<part name="body" element="tns:BrowseNodeLookup"/>
    </message>
    <message name="BrowseNodeLookupResponseMsg">
	<part name="body" element="tns:BrowseNodeLookupResponse"/>
    </message>
    <message name="ListSearchRequestMsg">
	<part name="body" element="tns:ListSearch"/>
    </message>
    <message name="ListSearchResponseMsg">
	<part name="body" element="tns:ListSearchResponse"/>
    </message>
    <message name="ListLookupRequestMsg">
	<part name="body" element="tns:ListLookup"/>
    </message>
    <message name="ListLookupResponseMsg">
	<part name="body" element="tns:ListLookupResponse"/>
    </message>
    <message name="CustomerContentSearchRequestMsg">
	<part name="body" element="tns:CustomerContentSearch"/>
    </message>
    <message name="CustomerContentSearchResponseMsg">
	<part name="body" element="tns:CustomerContentSearchResponse"/>
    </message>
    <message name="CustomerContentLookupRequestMsg">
	<part name="body" element="tns:CustomerContentLookup"/>
    </message>
    <message name="CustomerContentLookupResponseMsg">
	<part name="body" element="tns:CustomerContentLookupResponse"/>
    </message>
    <message name="SimilarityLookupRequestMsg">
	<part name="body" element="tns:SimilarityLookup"/>
    </message>
    <message name="SimilarityLookupResponseMsg">
	<part name="body" element="tns:SimilarityLookupResponse"/>
    </message>
    <message name="SellerLookupRequestMsg">
	<part name="body" element="tns:SellerLookup"/>
    </message>
    <message name="SellerLookupResponseMsg">
	<part name="body" element="tns:SellerLookupResponse"/>
    </message>
    <message name="CartGetRequestMsg">
	<part name="body" element="tns:CartGet"/>
    </message>
    <message name="CartGetResponseMsg">
	<part name="body" element="tns:CartGetResponse"/>
    </message>
    <message name="CartAddRequestMsg">
	<part name="body" element="tns:CartAdd"/>
    </message>
    <message name="CartAddResponseMsg">
	<part name="body" element="tns:CartAddResponse"/>
    </message>
    <message name="CartCreateRequestMsg">
	<part name="body" element="tns:CartCreate"/>
    </message>
    <message name="CartCreateResponseMsg">
	<part name="body" element="tns:CartCreateResponse"/>
    </message>
    <message name="CartModifyRequestMsg">
	<part name="body" element="tns:CartModify"/>
    </message>
    <message name="CartModifyResponseMsg">
	<part name="body" element="tns:CartModifyResponse"/>
    </message>
    <message name="CartClearRequestMsg">
	<part name="body" element="tns:CartClear"/>
    </message>
    <message name="CartClearResponseMsg">
	<part name="body" element="tns:CartClearResponse"/>
    </message>
    <message name="TransactionLookupRequestMsg">
	<part name="body" element="tns:TransactionLookup"/>
    </message>
    <message name="TransactionLookupResponseMsg">
	<part name="body" element="tns:TransactionLookupResponse"/>
    </message>
    <message name="SellerListingSearchRequestMsg">
	<part name="body" element="tns:SellerListingSearch"/>
    </message>
    <message name="SellerListingSearchResponseMsg">
	<part name="body" element="tns:SellerListingSearchResponse"/>
    </message>
    <message name="SellerListingLookupRequestMsg">
	<part name="body" element="tns:SellerListingLookup"/>
    </message>
    <message name="TagLookupRequestMsg">
	<part name="body" element="tns:TagLookup"/>
    </message>
    <message name="TagLookupResponseMsg">
	<part name="body" element="tns:TagLookupResponse"/>
    </message>
    <message name="SellerListingLookupResponseMsg">
	<part name="body" element="tns:SellerListingLookupResponse"/>
    </message>
    <message name="VehicleSearchRequestMsg">
	<part name="body" element="tns:VehicleSearch"/>
    </message>
    <message name="VehicleSearchResponseMsg">
	<part name="body" element="tns:VehicleSearchResponse"/>
    </message>
    <message name="VehiclePartSearchRequestMsg">
	<part name="body" element="tns:VehiclePartSearch"/>
    </message>
    <message name="VehiclePartSearchResponseMsg">
	<part name="body" element="tns:VehiclePartSearchResponse"/>
    </message>
    <message name="VehiclePartLookupRequestMsg">
	<part name="body" element="tns:VehiclePartLookup"/>
    </message>
    <message name="VehiclePartLookupResponseMsg">
	<part name="body" element="tns:VehiclePartLookupResponse"/>
    </message>
    <message name="MultiOperationRequestMsg">
	<part name="body" element="tns:MultiOperation"/>
    </message>
    <message name="MultiOperationResponseMsg">
	<part name="body" element="tns:MultiOperationResponse"/>
    </message>
    <portType name="AWSECommerceServicePortType">
	<operation name="Help">
	    <input message="tns:HelpRequestMsg"/>
	    <output message="tns:HelpResponseMsg"/>
	</operation>
	<operation name="ItemSearch">
	    <input message="tns:ItemSearchRequestMsg"/>
	    <output message="tns:ItemSearchResponseMsg"/>
	</operation>
	<operation name="ItemLookup">
	    <input message="tns:ItemLookupRequestMsg"/>
	    <output message="tns:ItemLookupResponseMsg"/>
	</operation>
	<operation name="BrowseNodeLookup">
	    <input message="tns:BrowseNodeLookupRequestMsg"/>
	    <output message="tns:BrowseNodeLookupResponseMsg"/>
	</operation>
	<operation name="ListSearch">
	    <input message="tns:ListSearchRequestMsg"/>
	    <output message="tns:ListSearchResponseMsg"/>
	</operation>
	<operation name="ListLookup">
	    <input message="tns:ListLookupRequestMsg"/>
	    <output message="tns:ListLookupResponseMsg"/>
	</operation>
	<operation name="CustomerContentSearch">
	    <input message="tns:CustomerContentSearchRequestMsg"/>
	    <output message="tns:CustomerContentSearchResponseMsg"/>
	</operation>
	<operation name="CustomerContentLookup">
	    <input message="tns:CustomerContentLookupRequestMsg"/>
	    <output message="tns:CustomerContentLookupResponseMsg"/>
	</operation>
	<operation name="SimilarityLookup">
	    <input message="tns:SimilarityLookupRequestMsg"/>
	    <output message="tns:SimilarityLookupResponseMsg"/>
	</operation>
	<operation name="SellerLookup">
	    <input message="tns:SellerLookupRequestMsg"/>
	    <output message="tns:SellerLookupResponseMsg"/>
	</operation>
	<operation name="CartGet">
	    <input message="tns:CartGetRequestMsg"/>
	    <output message="tns:CartGetResponseMsg"/>
	</operation>
	<operation name="CartAdd">
	    <input message="tns:CartAddRequestMsg"/>
	    <output message="tns:CartAddResponseMsg"/>
	</operation>
	<operation name="CartCreate">
	    <input message="tns:CartCreateRequestMsg"/>
	    <output message="tns:CartCreateResponseMsg"/>
	</operation>
	<operation name="CartModify">
	    <input message="tns:CartModifyRequestMsg"/>
	    <output message="tns:CartModifyResponseMsg"/>
	</operation>
	<operation name="CartClear">
	    <input message="tns:CartClearRequestMsg"/>
	    <output message="tns:CartClearResponseMsg"/>
	</operation>
	<operation name="TransactionLookup">
	    <input message="tns:TransactionLookupRequestMsg"/>
	    <output message="tns:TransactionLookupResponseMsg"/>
	</operation>
	<operation name="SellerListingSearch">
	    <input message="tns:SellerListingSearchRequestMsg"/>
	    <output message="tns:SellerListingSearchResponseMsg"/>
	</operation>
	<operation name="SellerListingLookup">
	    <input message="tns:SellerListingLookupRequestMsg"/>
	    <output message="tns:SellerListingLookupResponseMsg"/>
	</operation>
	<operation name="TagLookup">
	    <input message="tns:TagLookupRequestMsg"/>
	    <output message="tns:TagLookupResponseMsg"/>
	</operation>
	<operation name="VehicleSearch">
	    <input message="tns:VehicleSearchRequestMsg"/>
	    <output message="tns:VehicleSearchResponseMsg"/>
	</operation>
	<operation name="VehiclePartSearch">
	    <input message="tns:VehiclePartSearchRequestMsg"/>
	    <output message="tns:VehiclePartSearchResponseMsg"/>
	</operation>
	<operation name="VehiclePartLookup">
	    <input message="tns:VehiclePartLookupRequestMsg"/>
	    <output message="tns:VehiclePartLookupResponseMsg"/>
	</operation>
	<operation name="MultiOperation">
	    <input message="tns:MultiOperationRequestMsg"/>
	    <output message="tns:MultiOperationResponseMsg"/>
	</operation>
    </portType>
    <binding name="AWSECommerceServiceBinding" type="tns:AWSECommerceServicePortType">
	<soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
	<operation name="Help">
	    <soap:operation soapAction="http://soap.amazon.com/Help"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="ItemSearch">
	    <soap:operation soapAction="http://soap.amazon.com/ItemSearch"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="ItemLookup">
	    <soap:operation soapAction="http://soap.amazon.com/ItemLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="BrowseNodeLookup">
	    <soap:operation soapAction="http://soap.amazon.com/BrowseNodeLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="ListSearch">
	    <soap:operation soapAction="http://soap.amazon.com/ListSearch"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="ListLookup">
	    <soap:operation soapAction="http://soap.amazon.com/ListLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CustomerContentSearch">
	    <soap:operation soapAction="http://soap.amazon.com/CustomerContentSearch"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CustomerContentLookup">
	    <soap:operation soapAction="http://soap.amazon.com/CustomerContentLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="SimilarityLookup">
	    <soap:operation soapAction="http://soap.amazon.com/SimilarityLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="SellerLookup">
	    <soap:operation soapAction="http://soap.amazon.com/SellerLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CartGet">
	    <soap:operation soapAction="http://soap.amazon.com/CartGet"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CartCreate">
	    <soap:operation soapAction="http://soap.amazon.com/CartCreate"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CartAdd">
	    <soap:operation soapAction="http://soap.amazon.com/CartAdd"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CartModify">
	    <soap:operation soapAction="http://soap.amazon.com/CartModify"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="CartClear">
	    <soap:operation soapAction="http://soap.amazon.com/CartClear"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="TransactionLookup">
	    <soap:operation soapAction="http://soap.amazon.com/TransactionLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="SellerListingSearch">
	    <soap:operation soapAction="http://soap.amazon.com/SellerListingSearch"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="SellerListingLookup">
	    <soap:operation soapAction="http://soap.amazon.com/SellerListingLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="TagLookup">
	    <soap:operation soapAction="http://soap.amazon.com/TagLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="VehicleSearch">
	    <soap:operation soapAction="http://soap.amazon.com/VehicleSearch"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="VehiclePartSearch">
	    <soap:operation soapAction="http://soap.amazon.com/VehiclePartSearch"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="VehiclePartLookup">
	    <soap:operation soapAction="http://soap.amazon.com/VehiclePartLookup"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
	<operation name="MultiOperation">
	    <soap:operation soapAction="http://soap.amazon.com/MultiOperation"/>
	    <input>
		<soap:body use="literal"/>
	    </input>
	    <output>
		<soap:body use="literal"/>
	    </output>
	</operation>
    </binding>
    <service name="AWSECommerceService">
	<port name="AWSECommerceServicePort" binding="tns:AWSECommerceServiceBinding">
	    <soap:address location="https://ecs.amazonaws.com/onca/soap?Service=AWSECommerceService"/>
	</port>
    </service>
</definitions>
"""))
Parser.version = '2009-11-01'
