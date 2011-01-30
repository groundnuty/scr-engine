I-Logix-RPY-Archive version 8.5.2 Java 2030848
{ IProject 
	- _id = GUID 091d9137-4a2a-46bd-ad3f-24f52771611f;
	- _myState = 8192;
	- _name = "scr-engine";
	- _lastID = 5;
	- _UserColors = { IRPYRawContainer 
		- size = 16;
		- value = 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 16777215; 
	}
	- _defaultSubsystem = { ISubsystemHandle 
		- _m2Class = "ISubsystem";
		- _filename = "Engine.sbs";
		- _subsystem = "";
		- _class = "";
		- _name = "Engine";
		- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
	}
	- _component = { IHandle 
		- _m2Class = "IComponent";
		- _filename = "Debug.cmp";
		- _subsystem = "";
		- _class = "";
		- _name = "Debug";
		- _id = GUID 9c1665db-ad26-4300-9ef9-88674ca70282;
	}
	- Multiplicities = { IRPYRawContainer 
		- size = 5;
		- value = 
		{ IMultiplicityItem 
			- _name = "1";
			- _count = 1;
		}
		{ IMultiplicityItem 
			- _name = "*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "0,1";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "1..*";
			- _count = -1;
		}
		{ IMultiplicityItem 
			- _name = "4";
			- _count = 0;
		}
	}
	- Subsystems = { IRPYRawContainer 
		- size = 3;
		- value = 
		{ IProfile 
			- fileName = "JavaDocProfile";
			- _persistAs = "$OMROOT\\Profiles\\JavaDoc\\";
			- _id = GUID 19700e28-456f-4c97-a19c-b95dcb3e9dff;
			- _isReference = 1;
		}
		{ ISubsystem 
			- fileName = "Engine";
			- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
		}
		{ IProfile 
			- fileName = "CGCompatibilityPre753Java";
			- _id = GUID 1a373eb2-7fe0-464e-80c5-32bbc6b2649c;
		}
	}
	- Diagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IDiagram 
			- _id = GUID 4e467583-4f1c-41f5-b91b-3066df3a5cc7;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 4;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Association";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Class";
								- Properties = { IRPYRawContainer 
									- size = 8;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Object";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,34,84,148";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Underline@Child.NameCompartment@Name";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "121,122,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Package";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,216,151";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "221,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Model";
			- _lastModifiedTime = "1.30.2011::0:16:41";
			- _graphicChart = { CGIClassChart 
				- _id = GUID aa167807-2d0c-4983-bdba-db3f0ac4dc5e;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IDiagram";
					- _id = GUID 4e467583-4f1c-41f5-b91b-3066df3a5cc7;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 10;
				{ CGIClass 
					- _id = GUID 56db2d29-8a9e-4e76-8209-337a597e58fc;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 4e1e93f9-a1c1-4821-bd27-1f313698e2a2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIPackage 
					- _id = GUID c905bf92-6d34-4730-a6b6-fb13fcf3b72d;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 127;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Engine.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Engine";
						- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
					}
					- m_pParent = GUID 56db2d29-8a9e-4e76-8209-337a597e58fc;
					- m_name = { CGIText 
						- m_str = "Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 4104;
					- m_transform = 0.863487 0 0 0.606429 86 22.057 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 0 0  0 1151  1216 1151  1216 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIAssociationEnd 
					- _id = GUID 6d6a1164-e6f6-4b6a-965d-32633cd95a05;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "itsThrottle";
						- _id = GUID 1a1e4f17-286a-4521-aedf-71fa4e738942;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4a3c6565-df46-4c00-860a-4fc4d84b4ece;
					- m_sourceType = 'F';
					- m_pTarget = GUID 90e2a891-a9a7-4ee1-8795-887e9d758759;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 632 800 ;
					- m_TargetPort = 396 979 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Throttle";
						- _name = "itsEngine";
						- _id = GUID c611146b-e01b-46c0-88b7-d93dcae92f46;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIAssociationEnd 
					- _id = GUID 5a6f0e5e-3fd0-42fd-a857-1ab3c08f3c3a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "itsFuelInjector";
						- _id = GUID ca7eec61-41bf-4a71-a0bc-e28b33676934;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4a3c6565-df46-4c00-860a-4fc4d84b4ece;
					- m_sourceType = 'F';
					- m_pTarget = GUID 80b98eb1-e0e4-42fe-a8e8-93c1b63b472f;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_arrow = 2 512 257  512 589  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 722 980 ;
					- m_TargetPort = 430 1008 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "FuelInjector";
						- _name = "itsEngine";
						- _id = GUID ff15137b-c10a-479b-9615-2f7cb9b75da6;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 6;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 4;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIObjectInstance 
					- _id = GUID 4a3c6565-df46-4c00-860a-4fc4d84b4ece;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 106;
					- m_pModelObject = { IHandle 
						- _m2Class = "IPart";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "EngineBuilder";
						- _name = "itsEngine";
						- _id = GUID 300889b3-33b8-48de-b16f-40a9aa74696b;
					}
					- m_pParent = GUID bfbc0cda-9072-42a1-93be-7704d8ac1b4a;
					- m_name = { CGIText 
						- m_str = "itsEngine:Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.26032 0 0 0.351265 63.2321 251.488 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "isStarted";
							- _id = GUID 0f843392-32bc-4877-ad3b-1f27085bc3b3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "rotationSpeed";
							- _id = GUID b7569414-1012-4339-acad-7267776a980a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "temperature";
							- _id = GUID 19110321-cf1b-4388-bb2d-6766d3b60126;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 7;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "getTemperature()";
							- _id = GUID eb167094-0934-4214-9214-cb4a3e130708;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "getRotationSpeed()";
							- _id = GUID 23ac84e7-6ef4-481e-9b80-fb69109c24d2;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "calculateOpeningDuration()";
							- _id = GUID 64ff4a23-4cc5-4b8e-b8d1-5875e9b4bb84;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "engineStopped()";
							- _id = GUID 718e31db-1e55-4326-b24d-5b25d978b200;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "engineStarted()";
							- _id = GUID 38d8a728-2d9e-4b45-b33b-9472d79a9702;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "conditionChanged()";
							- _id = GUID 8d663350-6ed3-4aa0-a5ff-f6b8342060d0;
						}
						{ IHandle 
							- _m2Class = "IConstructor";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Engine";
							- _name = "Engine()";
							- _id = GUID 1e3a3d84-8974-4340-bca6-8c3b5da8314a;
						}
					}
					- m_multiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
				}
				{ CGIObjectInstance 
					- _id = GUID 90e2a891-a9a7-4ee1-8795-887e9d758759;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 106;
					- m_pModelObject = { IHandle 
						- _m2Class = "IPart";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "EngineBuilder";
						- _name = "itsThrottle";
						- _id = GUID 390ad76b-77b8-400e-a103-9ad06a866aef;
					}
					- m_pParent = GUID bfbc0cda-9072-42a1-93be-7704d8ac1b4a;
					- m_name = { CGIText 
						- m_str = "itsThrottle:Throttle";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.246707 0 0 0.266963 758.76 276.597 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Throttle";
							- _name = "getPressing()";
							- _id = GUID e7f6982b-e785-4bcd-bec0-cdca7990200c;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Throttle";
							- _name = "setPressing(int)";
							- _id = GUID 49c74bd5-cb84-49d3-a1dd-d7d86f4a5fea;
						}
						{ IHandle 
							- _m2Class = "IConstructor";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "Throttle";
							- _name = "Throttle()";
							- _id = GUID b0b46a45-e662-4a51-b54d-ba4a9f0065d8;
						}
					}
					- m_multiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
				}
				{ CGIObjectInstance 
					- _id = GUID a7d21044-c491-461f-a888-e7d1ce2273a3;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 106;
					- m_pModelObject = { IHandle 
						- _m2Class = "IPart";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "EngineBuilder";
						- _name = "itsSparkPlug";
						- _id = GUID 8a33168a-b8f8-4e2b-a12e-05a8207fb759;
					}
					- m_pParent = GUID bfbc0cda-9072-42a1-93be-7704d8ac1b4a;
					- m_name = { CGIText 
						- m_str = "itsSparkPlug:SparkPlug";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.324974 0 0 0.318481 64.9029 858.689 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=50%,50%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 3;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "number";
							- _id = GUID 9c056b56-75fc-40bb-8647-d691f2e48e27;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "sparkDelay";
							- _id = GUID 4e97b6fd-64c7-493d-9e9f-b00c229cde9a;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "sparkWait";
							- _id = GUID 818e789d-54b8-4302-b776-98932fc6d692;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "makeSpark()";
							- _id = GUID 325a26a6-6abd-4f05-ad11-8cad94a44a28;
						}
						{ IHandle 
							- _m2Class = "IConstructor";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "SparkPlug(int)";
							- _id = GUID e2ebeb24-4a85-4c46-a494-e8e5033d4db3;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "setSparkDelay(int)";
							- _id = GUID e9c23d90-6a7b-41d1-805d-79729c179a42;
						}
						{ IHandle 
							- _m2Class = "IConstructor";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "SparkPlug()";
							- _id = GUID 5677dd80-c247-41e9-b105-741d16c08c22;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "engineStarted()";
							- _id = GUID 5f3c75d1-0c19-472f-be53-9c49eafce07a;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "SparkPlug";
							- _name = "engineStopped()";
							- _id = GUID 746de3d9-b183-4598-ae6d-642206eec046;
						}
					}
					- m_multiplicity = { CGIText 
						- m_str = "4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
				}
				{ CGIObjectInstance 
					- _id = GUID 80b98eb1-e0e4-42fe-a8e8-93c1b63b472f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 106;
					- m_pModelObject = { IHandle 
						- _m2Class = "IPart";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "EngineBuilder";
						- _name = "itsFuelInjector";
						- _id = GUID 40dd2104-4840-44d6-8399-360aac37be56;
					}
					- m_pParent = GUID bfbc0cda-9072-42a1-93be-7704d8ac1b4a;
					- m_name = { CGIText 
						- m_str = "itsFuelInjector:FuelInjector";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2824;
					- m_transform = 0.362405 0 0 0.266963 681.049 930.836 ;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_bFramesetModified = 1;
					- m_polygon = 4 2 329  2 1451  1061 1451  1061 329  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- frameset = "<frameset rows=47%,53%>
<frame name=AttributeListCompartment>
<frame name=PrimitiveOperationListCompartment>";
					- Attrs = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "openingTime";
							- _id = GUID 2555e3ab-b75a-426b-a8c6-3dfa9bcda4f3;
						}
						{ IHandle 
							- _m2Class = "IAttribute";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "delayTime";
							- _id = GUID 390f51b0-8f99-447b-9353-97218a103438;
						}
					}
					- Operations = { IRPYRawContainer 
						- size = 6;
						- value = 
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "open()";
							- _id = GUID e1e62c18-2c2e-4646-b2ed-445ab27485ff;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "close()";
							- _id = GUID e682cd40-ea23-4016-8d56-e8013624a38e;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "setOpeningTime(int)";
							- _id = GUID 2f1891d3-65ca-485f-9ae1-144cbbb37d1b;
						}
						{ IHandle 
							- _m2Class = "IPrimitiveOperation";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "setDelayTime(int)";
							- _id = GUID d19192d0-f85d-4093-a0c8-d48030d38ab1;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "engineStopped()";
							- _id = GUID da650b57-79d9-4221-ada0-78696c1c136f;
						}
						{ IHandle 
							- _m2Class = "IReception";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "FuelInjector";
							- _name = "engineStarted()";
							- _id = GUID 338e8a20-b35a-4765-8fb1-da5464dbdf86;
						}
					}
					- m_multiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
				}
				{ CGIAssociationEnd 
					- _id = GUID 38d74c09-bc3f-4250-a562-c8d3d61c1e63;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 92;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "itsSparkPlug";
						- _id = GUID ba5029b4-c745-456c-9662-a99044962186;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 4a3c6565-df46-4c00-860a-4fc4d84b4ece;
					- m_sourceType = 'F';
					- m_pTarget = GUID a7d21044-c491-461f-a888-e7d1ce2273a3;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 7;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 632 1301 ;
					- m_TargetPort = 501 651 ;
					- m_pInverseModelObject = { IAssociationEndHandle 
						- _m2Class = "IAssociationEnd";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "SparkPlug";
						- _name = "itsEngine_3";
						- _id = GUID e3b033ea-b43c-4c32-9d0a-09100f45c9e2;
					}
					- m_pInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_pInverseInstance = { IObjectLinkHandle 
						- _m2Class = "";
					}
					- m_bShowSourceMultiplicity = 1;
					- m_bShowSourceRole = 0;
					- m_bShowTargetMultiplicity = 1;
					- m_bShowTargetRole = 0;
					- m_bShowLinkName = 1;
					- m_bShowSpecificType = 0;
					- m_bInstance = 0;
					- m_bShowQualifier1 = 1;
					- m_bShowQualifier2 = 1;
					- m_sourceRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 2;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_targetRole = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 3;
						- m_bImplicitSetRectPoints = 0;
					}
					- m_sourceMultiplicity = { CGIText 
						- m_str = "1";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 4;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 0;
					}
					- m_targetMultiplicity = { CGIText 
						- m_str = "4";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  14 -9  14 9  -6 9  ;
						- m_nIdent = 5;
						- m_bImplicitSetRectPoints = 1;
						- m_transform = 0.7 0 0 1 255.2 264 ;
						- m_nOrientationCtrlPt = 6;
					}
					- m_sourceQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 6;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_targetQualifier = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 7;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_specificType = symmetric_type;
				}
				{ CGIClass 
					- _id = GUID bfbc0cda-9072-42a1-93be-7704d8ac1b4a;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 105;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "";
						- _name = "EngineBuilder";
						- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
					}
					- m_pParent = GUID c905bf92-6d34-4730-a6b6-fb13fcf3b72d;
					- m_name = { CGIText 
						- m_str = "EngineBuilder";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.899427 0 0 0.907309 88.3184 -153.175 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 3 265  3 1410  1195 1410  1195 265  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 56db2d29-8a9e-4e76-8209-337a597e58fc;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Engine.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Engine";
				- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
			}
		}
	}
	- Components = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IComponent 
			- fileName = "Debug";
			- _id = GUID 9c1665db-ad26-4300-9ef9-88674ca70282;
		}
	}
	- UCDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IUCDiagram 
			- _id = GUID 7f4b5b3a-4f71-48f7-b598-31e0c586c392;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 5;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "Actor";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,26,84,168";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Depends";
								- Properties = { IRPYRawContainer 
									- size = 6;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineStyle";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "Inheritance";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,128";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,16,230";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "System_Border";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,228,240";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "UseCase";
								- Properties = { IRPYRawContainer 
									- size = 7;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,21,129,92";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.FillColor";
										- _Value = "255,255,255";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.FontColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "111,0,107";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "Engine Use Case";
			- _lastModifiedTime = "1.30.2011::0:22:25";
			- _graphicChart = { CGIClassChart 
				- _id = GUID d193d115-a9ea-48a4-893f-22c89907550b;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IUCDiagram";
					- _id = GUID 7f4b5b3a-4f71-48f7-b598-31e0c586c392;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 18;
				{ CGIClass 
					- _id = GUID fb9b259d-d470-4503-80df-0921cd09721b;
					- m_type = 78;
					- m_pModelObject = { IHandle 
						- _m2Class = "IClass";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "";
						- _name = "TopLevel";
						- _id = GUID 4e1e93f9-a1c1-4821-bd27-1f313698e2a2;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "TopLevel";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- Attrs = { IRPYRawContainer 
						- size = 0;
					}
					- Operations = { IRPYRawContainer 
						- size = 0;
					}
				}
				{ CGIInheritance 
					- _id = GUID b8697dd7-eb03-4cca-bc11-28419df4f1c0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Speed Up";
						- _name = "Change fuel input rate";
						- _id = GUID 9a2e54ce-dad3-4a33-8807-96ef86829ea0;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 3f2e83ff-8e75-4e59-b0bc-0087bf181751;
					- m_sourceType = 'F';
					- m_pTarget = GUID a7523b84-bf85-4757-bec9-9025ded5642c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 451 411  451 446  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 870 708 ;
					- m_TargetPort = -2 648 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID fe8e0aac-41b6-43eb-9873-37a9fe7b022f;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Slow down";
						- _name = "Change fuel input rate";
						- _id = GUID 1a8e99e8-b54c-4d7e-ac1a-09d8788ff56a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 7e1eab56-4874-4402-b388-72ea1b04081b;
					- m_sourceType = 'F';
					- m_pTarget = GUID a7523b84-bf85-4757-bec9-9025ded5642c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 451 480  451 446  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 870 512 ;
					- m_TargetPort = -2 648 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 030d6907-bde8-4f8a-8e0a-f250d3726c27;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
											{ IProperty 
												- _Name = "TreeStyle";
												- _Value = "True";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 103;
					- m_pModelObject = { IHandle 
						- _m2Class = "IGeneralization";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Stop Engine";
						- _name = "Change fuel input rate";
						- _id = GUID 4ff29374-eba8-4378-8f8b-22b5f76b1806;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID b4c34611-49ed-4993-bd72-cbcc2bd1ea77;
					- m_sourceType = 'F';
					- m_pTarget = GUID a7523b84-bf85-4757-bec9-9025ded5642c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_arrow = 2 451 585  451 446  ;
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 2;
					- m_SourcePort = 668 723 ;
					- m_TargetPort = -2 648 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID af48f58e-a92c-4c58-997c-278cb7a78f0c;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Start Engine";
						- _name = "Change fuel input rate";
						- _id = GUID 6aa75eb9-d261-45a9-8ac7-8e797c1fea0a;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Change fuel input rate";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 53b30c73-b0c0-41ac-acbf-4e3c1715dabf;
					- m_sourceType = 'F';
					- m_pTarget = GUID a7523b84-bf85-4757-bec9-9025ded5642c;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 878 612 ;
					- m_TargetPort = 749 572 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 5de73a3d-4f5b-46d9-981c-d2d584436538;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Start Engine";
						- _name = "Suplly power for first cycle";
						- _id = GUID 332b4e2c-de2e-4159-b08d-aa3357d1e40b;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Suplly power for first cycle";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 53b30c73-b0c0-41ac-acbf-4e3c1715dabf;
					- m_sourceType = 'F';
					- m_pTarget = GUID dae33cd1-4e66-49d3-9768-1f12b13f00b9;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "include";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 1049 628 ;
					- m_TargetPort = 374 572 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 4d669059-288d-41bb-92f1-7bfee0c90734;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Driver";
						- _name = "Start Engine";
						- _id = GUID 51f35312-1d93-4f53-ab8f-6c04006b3527;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Start Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1a25b23f-f0bd-4e5f-af6d-75dffed29976;
					- m_sourceType = 'F';
					- m_pTarget = GUID 53b30c73-b0c0-41ac-acbf-4e3c1715dabf;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 568 726 ;
					- m_TargetPort = 276 738 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 6f7ad5f1-3420-4852-9a28-3e3e27c25671;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Driver";
						- _name = "Speed Up";
						- _id = GUID 323a0a7e-0c7d-4b89-b1d0-f3efd82e14eb;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Speed Up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1a25b23f-f0bd-4e5f-af6d-75dffed29976;
					- m_sourceType = 'F';
					- m_pTarget = GUID 3f2e83ff-8e75-4e59-b0bc-0087bf181751;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 633 888 ;
					- m_TargetPort = 73 648 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID d87777d8-8465-492e-a232-c01ca1b4e9e2;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Driver";
						- _name = "Slow down";
						- _id = GUID d4715ffb-8b9d-432f-8d58-32663e49a1af;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Slow down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1a25b23f-f0bd-4e5f-af6d-75dffed29976;
					- m_sourceType = 'F';
					- m_pTarget = GUID 7e1eab56-4874-4402-b388-72ea1b04081b;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 826 1081 ;
					- m_TargetPort = 166 391 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIInheritance 
					- _id = GUID 5a2671be-2924-475a-a0a1-d5ba1f6dc922;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ShowLabels";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 128;
					- m_pModelObject = { IHandle 
						- _m2Class = "IDependency";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "Driver";
						- _name = "Stop Engine";
						- _id = GUID f404d9ce-68ab-4a63-b5a6-b3bbd24dd6be;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "Stop Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 8;
					- m_bIsPreferencesInitialized = 1;
					- m_pSource = GUID 1a25b23f-f0bd-4e5f-af6d-75dffed29976;
					- m_sourceType = 'F';
					- m_pTarget = GUID b4c34611-49ed-4993-bd72-cbcc2bd1ea77;
					- m_targetType = 'T';
					- m_direction = ' ';
					- m_rpn = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_anglePoint1 = 0 0 ;
					- m_anglePoint2 = 0 0 ;
					- m_line_style = 0;
					- m_SourcePort = 864 1340 ;
					- m_TargetPort = 288 527 ;
					- m_ShowName = 0;
					- m_ShowStereotype = 1;
				}
				{ CGIBox 
					- _id = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "General";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Graphics";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "FitBoxToItsTextuals";
												- _Value = "False";
												- _Type = Bool;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 123;
					- m_pModelObject = { IHandle 
						- _m2Class = "";
					}
					- m_pParent = GUID fb9b259d-d470-4503-80df-0921cd09721b;
					- m_name = { CGIText 
						- m_str = "Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.385179 0 0 0.454032 258 218 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 0  0 1240  1228 1240  1228 0  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID b4c34611-49ed-4993-bd72-cbcc2bd1ea77;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Stop Engine";
						- _id = GUID 2a5a7ad1-ecb2-4672-983e-13c249d481c9;
					}
					- m_pParent = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- m_name = { CGIText 
						- m_str = "Default::Stop Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.280189 0 0 0.14601 62.1272 702.739 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 3f2e83ff-8e75-4e59-b0bc-0087bf181751;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Speed Up";
						- _id = GUID f8c304ae-0fd3-41ee-a8af-0c165e024981;
					}
					- m_pParent = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- m_name = { CGIText 
						- m_str = "Default::Speed Up";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.280189 0 0 0.14601 52.3184 321.709 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 7e1eab56-4874-4402-b388-72ea1b04081b;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Slow down";
						- _id = GUID f568718f-5705-4ce3-822f-1ff4e3fe9818;
					}
					- m_pParent = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- m_name = { CGIText 
						- m_str = "Default::Slow down";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.280189 0 0 0.14601 54.7707 502.313 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID a7523b84-bf85-4757-bec9-9025ded5642c;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Change fuel input rate";
						- _id = GUID a1ca8f54-975a-48f0-822e-17ce9b7d7cbb;
					}
					- m_pParent = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- m_name = { CGIText 
						- m_str = "Default::Change fuel input rate";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.280189 0 0 0.14601 688.42 407.606 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 53b30c73-b0c0-41ac-acbf-4e3c1715dabf;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Start Engine";
						- _id = GUID 1a574265-e047-40f1-acff-8fa197fd19ac;
					}
					- m_pParent = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- m_name = { CGIText 
						- m_str = "Default::Start Engine";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.258469 0 0 0.139467 61.1789 123.916 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID dae33cd1-4e66-49d3-9768-1f12b13f00b9;
					- m_type = 125;
					- m_pModelObject = { IHandle 
						- _m2Class = "IUseCase";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Suplly power for first cycle";
						- _id = GUID d391117f-8d85-403b-aa41-129e5f393761;
					}
					- m_pParent = GUID ee01e796-0dc1-4e6d-bb84-22cb8ac20f95;
					- m_name = { CGIText 
						- m_str = "Default::Suplly power for first cycle";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.296642 0 0 0.14601 589.93 112.473 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 -2 -1  -2 1070  1127 1070  1127 -1  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIBasicClass 
					- _id = GUID 1a25b23f-f0bd-4e5f-af6d-75dffed29976;
					- m_type = 124;
					- m_pModelObject = { IHandle 
						- _m2Class = "IActor";
						- _filename = "";
						- _subsystem = "Default";
						- _class = "";
						- _name = "Driver";
						- _id = GUID a76dc546-2c74-449a-b0fb-3f18cc0763a8;
					}
					- m_pParent = GUID fb9b259d-d470-4503-80df-0921cd09721b;
					- m_name = { CGIText 
						- m_str = "Default::Driver";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 5;
					}
					- m_drawBehavior = 2056;
					- m_transform = 0.077634 0 0 0.123909 115.895 328.023 ;
					- m_bIsPreferencesInitialized = 1;
					- m_AdditionalLabel = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_polygon = 4 40 250  40 1396  1122 1396  1122 250  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID fb9b259d-d470-4503-80df-0921cd09721b;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Engine.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Engine";
				- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
			}
		}
	}
	- PanelDiagrams = { IRPYRawContainer 
		- size = 1;
		- value = 
		{ IPanelDiagram 
			- _id = GUID af46ad78-c6b8-42af-96de-0afcd2b5564b;
			- _myState = 8192;
			- _properties = { IPropertyContainer 
				- Subjects = { IRPYRawContainer 
					- size = 1;
					- value = 
					{ IPropertySubject 
						- _Name = "Format";
						- Metaclasses = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertyMetaclass 
								- _Name = "FreeText";
								- Properties = { IRPYRawContainer 
									- size = 9;
									- value = 
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Font";
										- _Value = "Arial";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Font.Height";
										- _Value = "13";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Font.Size";
										- _Value = "10";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "HorzAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Multiline";
										- _Value = "True";
										- _Type = Bool;
									}
									{ IProperty 
										- _Name = "VertAlign";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Wordbreak";
										- _Value = "False";
										- _Type = Bool;
									}
								}
							}
							{ IPropertyMetaclass 
								- _Name = "PushButton";
								- Properties = { IRPYRawContainer 
									- size = 5;
									- value = 
									{ IProperty 
										- _Name = "DefaultSize";
										- _Value = "0,0,100,50";
										- _Type = String;
									}
									{ IProperty 
										- _Name = "Fill.Transparent_Fill";
										- _Value = "1";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.LineColor";
										- _Value = "0,0,0";
										- _Type = Color;
									}
									{ IProperty 
										- _Name = "Line.LineWidth";
										- _Value = "0";
										- _Type = Int;
									}
									{ IProperty 
										- _Name = "Line.Transparent";
										- _Value = "1";
										- _Type = Int;
									}
								}
							}
						}
					}
				}
			}
			- _name = "EngineControl";
			- _lastModifiedTime = "1.30.2011::0:22:37";
			- _graphicChart = { CGIClassChart 
				- _id = GUID dca35c6c-7507-497a-bacf-7b99e80cee47;
				- m_type = 0;
				- m_pModelObject = { IHandle 
					- _m2Class = "IPanelDiagram";
					- _id = GUID af46ad78-c6b8-42af-96de-0afcd2b5564b;
				}
				- m_pParent = ;
				- m_name = { CGIText 
					- m_str = "";
					- m_style = "Arial" 10 0 0 0 1 ;
					- m_color = { IColor 
						- m_fgColor = 0;
						- m_bgColor = 0;
						- m_bgFlag = 0;
					}
					- m_position = 1 0 0  ;
					- m_nIdent = 0;
					- m_bImplicitSetRectPoints = 0;
					- m_nOrientationCtrlPt = 8;
				}
				- m_drawBehavior = 0;
				- m_bIsPreferencesInitialized = 0;
				- elementList = 10;
				{ CGIBox 
					- _id = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_type = 215;
					- m_pModelObject = { IHandle 
						- _m2Class = "ISubsystem";
						- _filename = "Engine.sbs";
						- _subsystem = "";
						- _class = "";
						- _name = "Engine";
						- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
					}
					- m_pParent = ;
					- m_name = { CGIText 
						- m_str = "";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 8;
					}
					- m_drawBehavior = 0;
					- m_bIsPreferencesInitialized = 0;
					- m_polygon = 0 ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
				}
				{ CGIActiveX 
					- _id = GUID dc8fd280-f88a-44b0-b8af-b165060ed856;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "OnOffSwitch";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 222;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "isStarted";
						- _id = GUID 0f843392-32bc-4877-ad3b-1f27085bc3b3;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "EngineState";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000485531 0 0 0.00043576 98 144.486 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsEngine.isStarted";
					- m_csName = "EngineState";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsEngine";
							- _id = GUID 300889b3-33b8-48de-b16f-40a9aa74696b;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 41a9bff5-1a5b-4db8-8098-2c029c2cdb30;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Slider";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Slider";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 225;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "temperature";
						- _id = GUID 19110321-cf1b-4388-bb2d-6766d3b60126;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "EngineTemperature";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00252476 0 0 0.000610064 69 364.68 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsEngine.temperature";
					- m_csName = "EngineTemperature";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsEngine";
							- _id = GUID 300889b3-33b8-48de-b16f-40a9aa74696b;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID fae8350c-b1e7-499a-84f4-2b0679292f0b;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Slider";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Slider";
										- Properties = { IRPYRawContainer 
											- size = 2;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
											{ IProperty 
												- _Name = "ShowName";
												- _Value = "Name";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 225;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "rotationSpeed";
						- _id = GUID b7569414-1012-4339-acad-7267776a980a;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "RotationSpeed";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00600116 0 0 0.000592634 68 252.66 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsEngine.rotationSpeed";
					- m_csName = "RotationSpeed";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsEngine";
							- _id = GUID 300889b3-33b8-48de-b16f-40a9aa74696b;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID 79391a49-8ff6-43bc-a299-79ba3286d8a7;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 2;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Slider";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Slider";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "Direction";
												- _Value = "InOut";
												- _Type = Enum;
												- _ExtraTypeInfo = "";
											}
										}
									}
								}
							}
						}
					}
					- m_type = 225;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Throttle";
						- _name = "pressing";
						- _id = GUID d95aa400-d9b7-4512-a77e-add554dc0049;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "ThrottlePressing";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00252476 0 0 0.000610064 425 368.68 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsThrottle.pressing";
					- m_csName = "ThrottlePressing";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsThrottle";
							- _id = GUID 390ad76b-77b8-400e-a103-9ad06a866aef;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID dcff72b3-7b4d-4819-a453-c14ea11cc889;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "Led";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 219;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "FuelInjector";
						- _name = "isOpen";
						- _id = GUID 67928a1e-2949-44d7-8775-637efdd70557;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "isOpen";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 4 -6 -9  51 -9  51 9  -6 9  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_transform = 1 0 0 1 282 34 ;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000126238 0 0 0.000113298 313 80.1262 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsFuelInjector.isOpen";
					- m_csName = "isOpen";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsFuelInjector";
							- _id = GUID 40dd2104-4840-44d6-8399-360aac37be56;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
				}
				{ CGIActiveX 
					- _id = GUID ab8ef7e8-fffa-47f8-834c-8f03feed22e0;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "FuelInjector";
						- _name = "openingTime";
						- _id = GUID 2555e3ab-b75a-426b-a8c6-3dfa9bcda4f3;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "Opening Time";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00157312 0 0 0.000278887 88 69.311 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsFuelInjector.openingTime";
					- m_csName = "Opening Time";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsFuelInjector";
							- _id = GUID 40dd2104-4840-44d6-8399-360aac37be56;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
				}
				{ CGIMFCCtrl 
					- _id = GUID d3618bc5-eb4f-4196-ad48-eca98c9ee920;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "engineStarted()";
						- _id = GUID 38d8a728-2d9e-4b45-b33b-9472d79a9702;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "start Engine
";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000971062 0 0 0.00043576 430 145.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsEngine.engineStarted";
					- m_csName = "start Engine
";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsEngine";
							- _id = GUID 300889b3-33b8-48de-b16f-40a9aa74696b;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
					- m_csButtonCaption = "Start engine";
				}
				{ CGIMFCCtrl 
					- _id = GUID cae5bb92-dcdf-4140-93bf-cb81d2ba8b92;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "PanelDiagram";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "PushButton";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ButtonFont";
												- _Value = "Arial 10 NoBold NoItalic";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 227;
					- m_pModelObject = { IHandle 
						- _m2Class = "IReception";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "Engine";
						- _name = "engineStopped()";
						- _id = GUID 718e31db-1e55-4326-b24d-5b25d978b200;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "stop Engine
";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.000971062 0 0 0.00043576 210 146.485 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.EngineBuilder[0].itsEngine.engineStopped";
					- m_csName = "stop Engine
";
					- m_PartsArray = { IRPYRawContainer 
						- size = 2;
						- value = 
						{ IHandle 
							- _m2Class = "IPart";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "EngineBuilder";
							- _name = "itsEngine";
							- _id = GUID 300889b3-33b8-48de-b16f-40a9aa74696b;
						}
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "EngineBuilder";
							- _id = GUID af5adf0a-720c-4d4e-84cc-51a768a9fc33;
						}
					}
					- m_csButtonCaption = "Stop engine";
				}
				{ CGIActiveX 
					- _id = GUID 06190b73-30e9-4edc-afde-bd46285da662;
					- _properties = { IPropertyContainer 
						- Subjects = { IRPYRawContainer 
							- size = 1;
							- value = 
							{ IPropertySubject 
								- _Name = "Format";
								- Metaclasses = { IRPYRawContainer 
									- size = 1;
									- value = 
									{ IPropertyMetaclass 
										- _Name = "DigitalDisplay";
										- Properties = { IRPYRawContainer 
											- size = 1;
											- value = 
											{ IProperty 
												- _Name = "ActiveXProperties@Child.ActiveXControl";
												- _Value = "";
												- _Type = String;
											}
										}
									}
								}
							}
						}
					}
					- m_type = 221;
					- m_pModelObject = { IHandle 
						- _m2Class = "IAttribute";
						- _filename = "Engine.sbs";
						- _subsystem = "Engine";
						- _class = "FuelInjector";
						- _name = "delayTime";
						- _id = GUID 390f51b0-8f99-447b-9353-97218a103438;
					}
					- m_pParent = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
					- m_name = { CGIText 
						- m_str = "Delay Time";
						- m_style = "Arial" 10 0 0 0 1 ;
						- m_color = { IColor 
							- m_fgColor = 0;
							- m_bgColor = 0;
							- m_bgFlag = 0;
						}
						- m_position = 1 0 0  ;
						- m_nIdent = 0;
						- m_bImplicitSetRectPoints = 0;
						- m_nOrientationCtrlPt = 1;
					}
					- m_drawBehavior = 4096;
					- m_transform = 0.00139833 0 0 0.000278887 380 66.3107 ;
					- m_bIsPreferencesInitialized = 1;
					- m_polygon = 4 0 -1114  0 113628  102980 113628  102980 -1114  ;
					- m_nNameFormat = 0;
					- m_nIsNameFormat = 0;
					- m_csModelObjPath = "Engine.FuelInjector[0].delayTime";
					- m_csName = "Delay Time";
					- m_PartsArray = { IRPYRawContainer 
						- size = 1;
						- value = 
						{ IHandle 
							- _m2Class = "IClass";
							- _filename = "Engine.sbs";
							- _subsystem = "Engine";
							- _class = "";
							- _name = "FuelInjector";
							- _id = GUID 70013ed4-ccd3-4a2a-aacd-96140f1e0131;
						}
					}
				}
				
				- m_access = 'Z';
				- m_modified = 'N';
				- m_fileVersion = "";
				- m_nModifyDate = 0;
				- m_nCreateDate = 0;
				- m_creator = "";
				- m_bScaleWithZoom = 1;
				- m_arrowStyle = 'S';
				- m_pRoot = GUID 0d73dbad-725c-4c23-9b20-2d0c346d7705;
				- m_currentLeftTop = 0 0 ;
				- m_currentRightBottom = 0 0 ;
			}
			- _defaultSubsystem = { IHandle 
				- _m2Class = "ISubsystem";
				- _filename = "Engine.sbs";
				- _subsystem = "";
				- _class = "";
				- _name = "Engine";
				- _id = GUID 3f8cd4a7-45a4-4b1c-aec0-4def943c5e34;
			}
		}
	}
}

